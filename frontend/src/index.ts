import Vue from "vue"
import * as VueGoogleMaps from "vue2-google-maps"
import HelloComponent from "./components/Hello.vue"
import Maps from "./components/Maps.vue"
import GMAPS_KEY from "./google_maps_key"


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
        <div>Hello {{name}}!</div>
        <hello-component :name="name" :initialEnthusiasm="5" />
        <maps />
    </div>`,
    data: {
        name: "World"
    },
    components: {
        HelloComponent,
        Maps
    }
});

