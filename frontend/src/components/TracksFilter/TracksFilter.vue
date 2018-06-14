<template>
  <div>
    <FilterOptions :filterMountains="filterMountains" />
    <FilterSort :sortMountains="sortMountains" />
    <ul>
      <li
        :key="index"
        v-for="({lat, lng, distance, name, elevation}, index) in mountains"
        style="padding: 5px;"
      >
        <p>Name: {{name}}</p>
        <p>Position: ({{lat}}, {{lng}})</p>
        <p>Elevation: {{elevation}}m</p>
        <p>Distance from your position: {{distance}}km</p>
      </li>
    </ul>
  </div>
</template>

<script lang="ts">
interface IPosition {
  lat: number
  lng: number
}
interface ITracksFilterInstance {
  reference?: IPosition
  distance?: number
  elevation?: number
  mountains: IMountainsFrontend[]
  skip: boolean
}

const mountainsQuery = require('../../queries/mountains.graphql')
import { ApolloQueryResult } from 'apollo-client'
import gql from 'graphql-tag'
import * as R from 'ramda'
import Vue from 'vue'
import { IMountainsFrontend } from '../../../typings/mountains'
import FilterOptions from './FilterOptions.vue'
import FilterSort from './FilterSort.vue'

export default Vue.extend({
  apollo: {
    mountains: {
      loadingKey: 'loading',
      query: mountainsQuery,
      variables() {
        const { distance, elevation, reference: { lat, lng } } = this
        return {
          distance,
          elevation,
          lat,
          lng,
        }
      },
      skip() {
        return this.skip
      },
    },
  },
  components: {
    FilterOptions,
  },
  computed: {
  },
  created() {
      // window.navigator.geolocation.getCurrentPosition(
      //   ({coords: {latitude: lat, longitude: lng}}) => {
      //     this.reference = {lat, lng}
      //   }
      // )
  },
  data(): ITracksFilterInstance {
      return {
        mountains: [] as IMountainsFrontend[],
        skip: true,
      }
  },
  methods: {
    filterMountains(distance: number, elevation: number): void {
      this.distance = distance
      this.elevation = elevation
      this.reference = {lat: -45, lng: -21}
      this.skip = false
      },
      sortMountains(distance: number, elevation: number): void {
      this.distance = distance
      this.elevation = elevation
      this.reference = {lat: -45, lng: -21}
      this.skip = false
      },
  },
  name: 'TracksFilter',
  props: [],
})
</script>

<style>
</style>