<template>
  <gmap-map
    :center="center"
    :zoom="7"
    map-type-id="terrain"
    style="width: 500px; height: 300px"
  >
    <gmap-marker
      :key="index"
      v-for="({name, elevation, lat, lng}, index) in mountains"
      :position="{lat, lng}"
      :clickable="true"
      :draggable="true"
      @click="center={lat, lng}"
    />
  </gmap-map>
</template>

<script lang="ts">
import Vue from "vue"
import gql from 'graphql-tag'
import * as R from 'ramda'
import { ApolloQueryResult } from 'apollo-client'
import { DataWithMountains } from '../queries/mountains'
import { MountainsGraphql, MountainsFrontend } from '../../typings/mountains'
const mountains = require('./mountains.graphql')

export default Vue.extend({
    props: [],
    data() {

        return {
          center: {lat: 10, lng: 10},
          mountains: [] as MountainsFrontend[],
        }
    },
    apollo: {
      mountains: {
        query: mountains,
        loadingKey: 'loading',
        result({ data: { mountains } } : ApolloQueryResult<DataWithMountains>) {
          this.mountains = R.map<MountainsGraphql, MountainsFrontend>(({properties: {name, elevation}, geometry: {coordinates: [lat, lng]}}) => {
            return {name, lat, lng, elevation}
          })(mountains)
        }
      }
    },
    methods: {
    },
    computed: {
    },
});
</script>

<style>
</style>