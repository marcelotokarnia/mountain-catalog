import App from '@components/App.vue'
import en from '@locales/en.json'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { ApolloClient } from 'apollo-client'
import { ApolloLink, concat, NextLink, Operation } from 'apollo-link'
import { HttpLink } from 'apollo-link-http'
import { withClientState } from 'apollo-link-state'
import Vue from 'vue'
import VueApollo from 'vue-apollo'
import * as VueIntl from 'vue-intl'
import * as VueGoogleMaps from 'vue2-google-maps'
import GMAPS_KEY from './google_maps_key'
import { defaults, resolvers } from './linkstate'

const link = new HttpLink({
    fetchOptions: {
        credentials: 'same-origin',
    },
    uri: '/graphql',
})

const authMiddleware = new ApolloLink((operation: Operation, forward?: NextLink) => {
    // add the authorization to the headers
    operation.setContext({
        headers: {
        'X-CSRFToken': CSRFTOKEN || 'csrf-token-not-set',
        },
    })
    return forward ? forward(operation) : null
    })

const cache = new InMemoryCache()

const stateLink = withClientState({
    cache,
    defaults,
    resolvers,
})

const apolloClient = new ApolloClient({
    cache,
    connectToDevTools: true,
    link: ApolloLink.from([stateLink, authMiddleware, link]),
})

const apolloProvider = new VueApollo({
    defaultClient: apolloClient,
})

Vue.use(VueApollo)

Vue.use(VueIntl)

Vue.setLocale('en')

Vue.registerMessages('en', en)

Vue.use(VueGoogleMaps, {
    load: {
        key: GMAPS_KEY,
        libraries: 'places',
    },
})

const v = new Vue({
    components: {
        App,
    },
    el: '#app',
    provide: apolloProvider.provide(),
    template: `<App />`,
})
