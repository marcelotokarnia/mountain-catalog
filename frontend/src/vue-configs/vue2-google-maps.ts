
import Vue from 'vue'
import * as VueGoogleMaps from 'vue2-google-maps'
import GMAPS_KEY from './google-maps-key'

Vue.use(VueGoogleMaps, {
  load: {
      key: GMAPS_KEY,
      libraries: 'places',
  },
})
