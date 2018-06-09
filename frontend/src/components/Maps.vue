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
      :draggable="false"
      @click="toggleInfoWindow(m, index)"
    />
  </gmap-map>
</template>

<script lang='ts'>
  interface Position {
    lat: number
    lng: number
  }

  interface MapsInstance {
    center: Position
    distance: number
    mountains: IMountainsFrontend[]
    infoWindowPos: Position
    currentMidx: number
    infoWinOpen: boolean
    infoContent1: string
    infoContent2: string
    infoOptions: object
    skip: boolean
  }

  import { ApolloQueryResult } from 'apollo-client'
  import gql from 'graphql-tag'
  import * as R from 'ramda'
  import Vue from 'vue'
  import { IMountainsFrontend, IMountainsGraphql } from '../../typings/mountains'
  import { IDataWithMountains } from '../queries/mountains'
  const mountains = require('../queries/mountains.graphql')

  export default Vue.extend({
      props: [],
      data(): MapsInstance {
          return {
            center: {lat: 10, lng: 10},
            distance: 5000,
            mountains: [] as IMountainsFrontend[],
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
              lng: this.center.lng,
            }
          },
          result({ data: { mountains } }: ApolloQueryResult<IDataWithMountains>) {
            this.mountains = R.map<IMountainsGraphql, IMountainsFrontend>(({properties: {distance, name, elevation}, geometry: {coordinates: [lat, lng]}}) => {
              return {name, lat, lng, elevation, distance}
            })(mountains)
          },
          skip() {
            return this.skip
          },
        },
      },
      methods: {
        toggleInfoWindow({lat, lng, name, elevation, distance}: IMountainsFrontend, idx: number): void {
          this.infoWindowPos = {lat, lng}
          this.infoContent1 = `${name}: ${elevation}m`
          this.infoContent2 = `${distance.toFixed(2)}km away`
          // check if its the same marker that was selected if yes toggle
          if (this.currentMidx == idx) {
            this.infoWinOpen = !this.infoWinOpen
          } else {
            this.infoWinOpen = true
            this.currentMidx = idx
          }
        },
      },
      computed: {
      },
      created() {
          window.navigator.geolocation.getCurrentPosition(
            ({coords: {latitude: lat, longitude: lng}}) => {
              this.center = {lat, lng}
              this.skip = false
            },
          )
      },
  })
</script>

<style>
</style>