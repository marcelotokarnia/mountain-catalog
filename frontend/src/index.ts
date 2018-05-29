import Vue from "vue"
import { ApolloClient } from 'apollo-client'
import { HttpLink } from 'apollo-link-http'
import { concat, ApolloLink, Operation, NextLink } from 'apollo-link'
import { InMemoryCache } from 'apollo-cache-inmemory'
import VueApollo from 'vue-apollo'
import * as VueGoogleMaps from "vue2-google-maps"
import Maps from "./components/Maps.vue"
import GMAPS_KEY from "./google_maps_key"

const link = new HttpLink({
    uri: 'http://localhost:8000/graphql',
    fetchOptions: {
        credentials: 'same-origin'
    }
})

const authMiddleware = new ApolloLink((operation: Operation, forward?: NextLink) => {
    // add the authorization to the headers
    operation.setContext({
      headers: {
        'X-CSRFToken': CSRFTOKEN,
      }
    })
    return forward ? forward(operation): null
  })

const apolloClient = new ApolloClient({
    link: concat(authMiddleware, link),
    cache: new InMemoryCache(),
    connectToDevTools: true,
})

const apolloProvider = new VueApollo({
    defaultClient: apolloClient,
})

Vue.use(VueApollo)

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


let v = new Vue({
    el: "#app",
    template: `
    <div>
        <maps />
    </div>`,
    data: {
        name: "World"
    },
    provide: apolloProvider.provide(),
    components: {
        Maps
    }
})

