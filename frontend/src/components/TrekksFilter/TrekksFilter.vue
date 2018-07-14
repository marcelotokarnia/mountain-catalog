<template>
  <div>
    <FilterOptions :filterMountains="filterMountains" />
    <FilterSort :sortMountains="sortMountains" />
    <MountainCard v-for="mountain in mountains" :key="mountain.id" :mountain="mountain" class="mb-2"/>
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
  mountains: IMountain[]
  smePosition?: IPosition
}

const mountainsQuery = require('@queries/mountains.graphql')
const mePositionQuery = require('@queries/mePositionState.graphql')
const mountainsMutation = require('@mutations/mountainsState.graphql')
import { IDataMountains, IMountain } from '@typings/mountains'
import { ApolloQueryResult } from 'apollo-client'
import gql from 'graphql-tag'
import * as R from 'ramda'
import Vue from 'vue'
import MountainCard from '@components/TrekksFilter/MountainCard.vue'
import FilterOptions from '@components/TrekksFilter/FilterOptions.vue'
import FilterSort from '@components/TrekksFilter/FilterSort.vue'

export default Vue.extend({
  apollo: {
    mountains: {
      loadingKey: 'loading',
      query: mountainsQuery,
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
        return true
      },
    },
    smePosition: {
      query: mePositionQuery,
      result( { data }:
        ApolloQueryResult<{smePosition: { position: IPosition } }>) {
        this.reference = data.smePosition.position
        if (this.distance && this.reference) {
          this.$apollo.queries.mountains.refetch({
            distance: {min: undefined, max: this.distance},
            elevation: {min: this.elevationMin, max: this.elevationMax},
            position: {lat: this.reference.lat, lng: this.reference.lng},
          })
          this.$apollo.queries.mountains.skip = false
        }
      },
    }
  },
  components: {
    FilterOptions,
    FilterSort,
    MountainCard,
  },
  computed: {
  },
  data(): ITracksFilterInstance {
      return {
        mountains: [] as IMountain[],
        smePosition: undefined,
        reference: undefined,
      }
  },
  methods: {
    filterMountains(distance: number, elevationMin: number, elevationMax: number): void {
      this.distance = distance
      this.elevationMin = elevationMin
      if (this.reference) {
        this.$apollo.queries.mountains.refetch({
          distance: {min: undefined, max: this.distance},
          elevation: {min: this.elevationMin, max: this.elevationMax},
          position: {lat: this.reference.lat, lng: this.reference.lng},
        })
        this.$apollo.queries.mountains.skip = false
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