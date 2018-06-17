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
      v-for="(m, index) in smountains"
      :position="{lat: m.lat, lng: m.lng}"
      :clickable="true"
      :draggable="false"
      @click="toggleInfoWindow(m, index)"
    />
  </gmap-map>
</template>

<script lang='ts'>
  interface IPosition {
    lat: number
    lng: number
  }

  interface IMapsInstance {
    center: IPosition
    smountains: IMountains[]
    infoWindowPos: IPosition
    currentMidx: number
    infoWinOpen: boolean
    infoContent1: string
    infoContent2: string
    infoOptions: object
    skip: boolean
  }

  import { IDataMountains, IMountains } from '@typings/mountains'
  import { ApolloQueryResult } from 'apollo-client'
  import gql from 'graphql-tag'
  import * as R from 'ramda'
  import Vue from 'vue'
  const mountainsState = require('../queries/mountainsState.graphql')

  export default Vue.extend({
    apollo: {
      smountains: {
        loadingKey: 'loading',
        query: mountainsState,
        skip() {
          return this.skip
        },
        result( { data: { smountains: { mountains } } }: ApolloQueryResult<any>) {
          this.smountains = mountains
        },
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
    data(): IMapsInstance {
        return {
          center: {lat: 10, lng: 10},
          currentMidx: 0,
          infoContent1: '',
          infoContent2: '',
          infoOptions: {
            pixelOffset: {
              height: -35,
              width: 0,
            },
          },
          infoWinOpen: false,
          infoWindowPos: {lat: 0, lng: 0},
          skip: true,
          smountains: [] as IMountains[],
        }
    },
    methods: {
      toggleInfoWindow({lat, lng, name, elevation, distance}: IMountains, idx: number): void {
        this.infoWindowPos = {lat, lng}
        this.infoContent1 = `${name}: ${elevation}m`
        this.infoContent2 = `${distance.toFixed(2)}km away`
        // check if its the same marker that was selected if yes toggle
        if (this.currentMidx === idx) {
          this.infoWinOpen = !this.infoWinOpen
        } else {
          this.infoWinOpen = true
          this.currentMidx = idx
        }
      },
    },
    name: 'Maps',
    props: [],
  })
</script>

<style>
</style>