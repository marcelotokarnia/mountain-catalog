<template>
  <form class="container">
    <div class="form-group">
      <label
        v-html="$formatMessage({id: 'trekks-filter.filter-sort.sorting'})" />
    </div>
    <div class="form-group row">
      <select v-model="sortBy" class="form-control col-6">
        <option value="elevation" v-html="$formatMessage({id: 'trekks-filter.filter-sort.elevation'})" />
        <option value="distance" v-html="$formatMessage({id: 'trekks-filter.filter-sort.distance'})" />
      </select>
      <select v-model="order" class="form-control col-6">
        <option value="" v-html="$formatMessage({id: 'trekks-filter.filter-sort.ascending'})" />
        <option value="-" v-html="$formatMessage({id: 'trekks-filter.filter-sort.descending'})" />
      </select>
    </div>
  </form>
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
  const mountains = require('@queries/mountainsState.graphql')

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