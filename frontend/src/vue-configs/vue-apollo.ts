import { defaults, resolvers } from '@src/linkstate'
import { InMemoryCache } from 'apollo-cache-inmemory'
import { ApolloClient } from 'apollo-client'
import { ApolloLink, concat, NextLink, Operation } from 'apollo-link'
import { HttpLink } from 'apollo-link-http'
import { withClientState } from 'apollo-link-state'
import Vue from 'vue'
import VueApollo from 'vue-apollo'

const link = new HttpLink({
  fetchOptions: {
      credentials: 'same-origin',
  },
  uri: '/graphql',
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
  link: ApolloLink.from([stateLink, link]),
})

const apolloProvider = new VueApollo({
  defaultClient: apolloClient,
})

Vue.use(VueApollo)

export default apolloProvider
