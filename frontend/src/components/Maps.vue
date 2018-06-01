<template>
  <gmap-map
    :center="center"
    :zoom="7"
    map-type-id="terrain"
    style="width: 500px; height: 300px"
  >
    <gmap-info-window
      :options="infoOptions"
      :position="infoWindowPos"
      :opened="infoWinOpen"
      @closeclick="infoWinOpen=false"
    >
      {{infoContent}}
    </gmap-info-window>

    <gmap-marker
      :key="index"
      v-for="(m, index) in mountains"
      :position="{lat: m.lat, lng: m.lng}"
      :clickable="true"
      :draggable="true"
      @click="toggleInfoWindow(m, index)"
    />
  </gmap-map>
</template>

<script lang="ts">
interface Position {
  lat: number
  lng: number
}
interface MapsInstance {
  center: Position
  distance: number
  mountains: MountainsFrontend[]
  infoWindowPos: Position
  currentMidx: number
  infoWinOpen: boolean
  infoContent: string
  infoOptions: object
  skip: boolean
}

import Vue from "vue"
import gql from 'graphql-tag'
import * as R from 'ramda'
import { ApolloQueryResult } from 'apollo-client'
import { DataWithMountains } from '../queries/mountains'
import { MountainsGraphql, MountainsFrontend } from '../../typings/mountains'
const mountains = require('../queries/mountains.graphql')

export default Vue.extend({
    props: [],
    data(): MapsInstance {
        return {
          center: {lat: 10, lng: 10},
          distance: 3500,
          mountains: [] as MountainsFrontend[],
          infoWindowPos: {lat: 0, lng: 0},
          currentMidx: 0,
          infoWinOpen: false,
          infoContent: '',
          skip: true,
          infoOptions: {
            pixelOffset: {
              width: 0,
              height: -35,
            },
          },

        }
    },
    apollo: {
      mountains: {
        query: mountains,
        loadingKey: 'loading',
        variables() {
          return {
            distance: this.distance,
            lat: this.center.lat,
            lng: this.center.lng
          }
        },
        result({ data: { mountains } } : ApolloQueryResult<DataWithMountains>) {
          this.mountains = R.map<MountainsGraphql, MountainsFrontend>(({properties: {name, elevation}, geometry: {coordinates: [lat, lng]}}) => {
            return {name, lat, lng, elevation}
          })(mountains)
        },
        skip() {
          return this.skip
        }
      }
    },
    methods: {
      toggleInfoWindow: function({lat, lng, name, elevation}: MountainsFrontend, idx: number): void {
        this.infoWindowPos = {lat, lng};
        this.infoContent = `${name}: ${elevation}m`;
        //check if its the same marker that was selected if yes toggle
        if (this.currentMidx == idx) {
          this.infoWinOpen = !this.infoWinOpen;
        }
        //if different marker set infowindow to open and reset current marker index
        else {
          this.infoWinOpen = true;
          this.currentMidx = idx;
        }
      }
    },
    computed: {
    },
    created: function(){
      	window.navigator.geolocation.getCurrentPosition(
          ({coords: {latitude: lat, longitude: lng}}) => {
            this.center = {lat, lng}
            this.skip = false
            // m.me = {windowOptions: {visible: false}, coords: angular.copy(m.map.center), key: 'me', options: {icon: '/static/icons/map_markers/bluedot.png'}}
          }
        )
    }
});
</script>

<style>
</style>