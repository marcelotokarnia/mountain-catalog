<template>
  <div>
    <select v-model="sortBy">
      <option value="elevation">Elevation</option>
      <option value="distance">Distance</option>
    </select>
    <select v-model="order">
      <option value="">Ascending</option>
      <option value="-">Descending</option>
    </select>
  </div>
</template>

<script lang="ts">
  interface IFilterSortInstance {
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
    computed: {},
      data(): IFilterSortInstance {
          return {
            order: '-',
            sortBy: 'elevation',
          }
      },
      methods: {
      },
      name: 'FilterSort',
      props: ['sortMountains'],
  })
</script>

<style>
</style>