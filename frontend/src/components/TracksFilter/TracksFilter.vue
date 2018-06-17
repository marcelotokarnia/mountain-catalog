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
  elevationMin?: number
  elevationMax?: number
  mountains: IMountains[]
  skip: boolean
}

const mountainsQuery = require('@queries/mountains.graphql')
const mountainsMutation = require('@mutations/mountains.graphql')
import { IDataMountains, IMountains } from '@typings/mountains'
import { ApolloQueryResult } from 'apollo-client'
import gql from 'graphql-tag'
import * as R from 'ramda'
import Vue from 'vue'
import FilterOptions from './FilterOptions.vue'
import FilterSort from './FilterSort.vue'

export default Vue.extend({
  apollo: {
    mountains: {
      loadingKey: 'loading',
      query: mountainsQuery,
      variables() {
        return {
          distance: this.distance,
          elevation: this.elevationMin,
          lat: this.reference.lat,
          lng: this.reference.lng,
        }
      },
      result( { data: { mountains } }: ApolloQueryResult<IDataMountains>) {
        this.mountains = mountains
        this.$apollo.mutate({
          mutation: mountainsMutation,
          variables: {
            mountains,
          },
        })
      },
      skip() {
        return this.skip
      },
    },
  },
  components: {
    FilterOptions,
    FilterSort,
  },
  computed: {
  },
  created() {
      window.navigator.geolocation.getCurrentPosition(
        ({coords: {latitude: lat, longitude: lng}}) => {
          this.reference = {lat, lng}
          if (this.distance) {
            this.skip = false
          }
        },
      )
  },
  data(): ITracksFilterInstance {
      return {
        mountains: [] as IMountains[],
        skip: true,
      }
  },
  methods: {
    filterMountains(distance: number, elevationMin: number, elevationMax: number): void {
      this.distance = distance
      this.elevationMin = elevationMin
      if (this.reference) {
        this.skip = false
        this.$apollo.queries.mountains.refetch({
          distance: this.distance,
          elevation: this.elevationMin,
          lat: this.reference.lat,
          lng: this.reference.lng,
        })
      }
    },
    sortMountains(distance: number, elevationMin: number): void {
      return
    },
  },
  name: 'TracksFilter',
  props: [],
})
</script>

<style>
</style>