<template>
  <gmap-map
    :center="{lat:10, lng:10}"
    :zoom="7"
    map-type-id="terrain"
    style="width: 500px; height: 300px"
  >
    <gmap-marker
      :key="index"
      v-for="(m, index) in markers"
      :position="m.position"
      :clickable="true"
      :draggable="true"
      @click="center=m.position"
    />
  </gmap-map>
</template>
<script lang="ts">
import Vue from "vue"

export default Vue.extend({
    props: [],
    data() {
        return {
          markers: [{position: {lat: 1.38, lng: 103.8}}, {position: {lat: 10, lng: 10}}]
        }
    },
    methods: {
    },
    computed: {
    },
});
</script>
<style>
</style>