<template>
  <select v-model="sortBy">
    <option value="elevation">Elevation</option>
    <option value="distance">Distance</option>
  </select>
  <select v-model="order">
    <option value="">Ascending</option>
    <option value="-">Descending</option>
  </select>
</template>

<script lang="ts">
interface FilterSortInstance {
  sortBy: string
  order: string
}

import { ApolloQueryResult } from 'apollo-client'
import gql from 'graphql-tag'
import * as R from 'ramda'
import Vue from 'vue'
import FilterOptions from './FilterOptions.vue'
const mountains = require('../../queries/mountains.graphql')

export default Vue.extend({
    props: ['sortMountains'],
    data(): FilterSortInstance {
        return {
          sortBy: 'elevation',
          order: '-',
        }
    },
    methods: {
    },
    computed: {
    },
    created() {
    },
})
</script>

<style>
</style>