<template>
  <div>
    <div>
      <label for="input-filter-distance">Maximum Distance</label>
      <input
        id="input-filter-distance"
        type="number"
        v-model="distance"
        @change="filterMountains(distance, elevation)"
      />
    </div>
    <div>
      <label for="input-filter-elevation">Minimum Elevation</label>
      <input
        id="input-filter-elevation"
        type="number"
        v-model="elevation"
        @change="filterMountains(distance, elevation)"
      />
    </div>
  </div>
</template>

<script lang="ts">
interface IFilterOptionsInstance {
  distance: number
  elevation: number
}

import { ApolloQueryResult } from 'apollo-client'
import gql from 'graphql-tag'
import * as R from 'ramda'
import Vue from 'vue'
import FilterOptions from './FilterOptions.vue'
const mountains = require('../../queries/mountains.graphql')

export default Vue.extend({
    data(): IFilterOptionsInstance {
        return {
          distance: 10000,
          elevation: 4000,
        }
    },
    computed: {
    },
    created() {
      this.filterMountains(this.distance, this.elevation)
    },
    methods: {
    },
    name: 'FilterOptions',
    props: ['filterMountains'],
})
</script>

<style>
</style>