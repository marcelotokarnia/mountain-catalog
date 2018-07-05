<template>
  <form>
    <div class="form-group">
      <label for="input-filter-distance"
        v-html="$formatMessage({id: 'trekks-filter.filter-options.maximum-distance'})" />
      <input
        class="form-control"
        id="input-filter-distance"
        type="number"
        v-model="distance"
        :placeholder="$formatMessage({id: 'trekks-filter.filter-options.maximum-distance'})"
        @change="filterMountains(+distance, +elevationMin)"
      />
    </div>
    <div class="form-group">
      <label for="input-filter-elevation"
        v-html="$formatMessage({id: 'trekks-filter.filter-options.minimum-elevation'})" />
      <input
        class="form-control"
        id="input-filter-elevation"
        type="number"
        v-model="elevationMin"
        :placeholder="$formatMessage({id: 'trekks-filter.filter-options.minimum-elevation'})"
        @change="filterMountains(+distance, +elevationMin)"
      />
    </div>
  </form>
</template>

<script lang="ts">
interface IFilterOptionsInstance {
  distance: number
  elevationMin: number
  elevationMax: number
}

import { ApolloQueryResult } from 'apollo-client'
import gql from 'graphql-tag'
import * as R from 'ramda'
import Vue from 'vue'
import FilterOptions from './FilterOptions.vue'
const mountains = require('@queries/mountains.graphql')

export default Vue.extend({
    data(): IFilterOptionsInstance {
        return {
          distance: 1000,
          elevationMax: 5000,
          elevationMin: 1000,
        }
    },
    computed: {
    },
    created() {
      const { distance, elevationMin, elevationMax } = this
      this.filterMountains(distance, elevationMin, elevationMax)
    },
    methods: {
    },
    name: 'FilterOptions',
    props: ['filterMountains'],
})
</script>