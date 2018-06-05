<template>
  <gmap-map
    :center="center"
    :zoom="5"
    map-type-id="terrain"
    style="width: 500px; height: 300px"
  >
    <gmap-info-window
      :options="infoOptions"
      :position="infoWindowPos"
      :opened="infoWinOpen"
      @closeclick="infoWinOpen=false"
    >
      <div>{{infoContent1}}</div>
      <div>{{infoContent2}}</div>
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
  infoContent1: string
  infoContent2: string
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
          distance: 5000,
          mountains: [] as MountainsFrontend[],
          infoWindowPos: {lat: 0, lng: 0},
          currentMidx: 0,
          infoWinOpen: false,
          infoContent1: '',
          infoContent2: '',
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
          this.mountains = R.map<MountainsGraphql, MountainsFrontend>(({properties: {distance, name, elevation}, geometry: {coordinates: [lat, lng]}}) => {
            return {name, lat, lng, elevation, distance}
          })(mountains)
        },
        skip() {
          return this.skip
        }
      }
    },
    methods: {
      toggleInfoWindow: function({lat, lng, name, elevation, distance}: MountainsFrontend, idx: number): void {
        this.infoWindowPos = {lat, lng};
        this.infoContent1 = `${name}: ${elevation}m`;
        this.infoContent2 = `${distance.toFixed(2)}km away`;
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
          }
        )
    }
});
</script>

<style>
</style>