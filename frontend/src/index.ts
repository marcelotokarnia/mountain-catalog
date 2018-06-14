import Maps from '@components/Maps.vue'
import TracksFilter from '@components/TracksFilter'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { ApolloClient } from 'apollo-client'
import { ApolloLink, concat, NextLink, Operation } from 'apollo-link'
import { HttpLink } from 'apollo-link-http'
import { withClientState } from 'apollo-link-state'
import Vue from 'vue'
import VueApollo from 'vue-apollo'
import * as VueGoogleMaps from 'vue2-google-maps'
import GMAPS_KEY from './google_maps_key'
import { resolvers, defaults } from './linkstate'

const HAS_NET = true

const link = new HttpLink({
    fetchOptions: {
        credentials: 'same-origin',
    },
    uri: 'http://localhost:8000/graphql',
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

if (HAS_NET) {
    Vue.use(VueGoogleMaps, {
        load: {
          key: GMAPS_KEY,
          libraries: 'places', // This is required if you use the Autocomplete plugin
          // OR: libraries: 'places,drawing'
          // OR: libraries: 'places,drawing,visualization'
          // (as you require)

          //// If you want to set the version, you can do so:
          // v: '3.26',
        },

        //// If you intend to programmatically custom event listener code
        //// (e.g. `this.$refs.gmap.$on('zoom_changed', someFunc)`)
        //// instead of going through Vue templates (e.g. `<GmapMap @zoom_changed="someFunc">`)
        //// you might need to turn this on.
        // autobindAllEvents: false,

        //// If you want to manually install components, e.g.
        //// import {GmapMarker} from 'vue2-google-maps/src/components/marker'
        //// Vue.component('GmapMarker', GmapMarker)
        //// then disable the following:
        // installComponents: true,
       })
}

const v = new Vue({
    components: {
        Maps,
        TracksFilter,
    },
    el: '#app',
    provide: apolloProvider.provide(),
    template: `
    <div>
        ${HAS_NET ? '<Maps />' : '<TracksFilter />'}
    </div>`,
})
