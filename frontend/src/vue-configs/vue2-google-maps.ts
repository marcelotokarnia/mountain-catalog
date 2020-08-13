import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps'

Vue.use(VueGoogleMaps, {
  load: {
    key: 'AIzaSyC_kmVi1Y-PEiJruIj2pGorJ7GPvy3j05Y',
    libraries: 'places',
  },
})
