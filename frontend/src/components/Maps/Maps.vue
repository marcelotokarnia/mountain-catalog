<template>
  <gmap-map
    :center="center"
    :zoom="5"
    map-type-id="terrain"
    style="width: 500px; height: 300px"
  >
    <TrekkInfo :mountain="selectedMountain" :isOpen="infoWinOpen" :onClose="closeInfo" />
    <gmap-marker
      :key="m.id"
      v-for="m in smountains"
      :position="{lat: m.position.lat, lng: m.position.lng}"
      :clickable="true"
      :draggable="false"
      @click="toggleInfoWindow(m)"
    />
  </gmap-map>
</template>

<script lang='ts'>
  interface IMapsInstance {
    center: IPosition
    smountains: IMountain[]
    selectedMountain?: IMountain
    infoWinOpen: boolean
  }

  import { IPosition } from '@typings/geo'
  import { IDataMountains, IMountain } from '@typings/mountains'
  import { ApolloQueryResult } from 'apollo-client'
  import gql from 'graphql-tag'
  import * as R from 'ramda'
  import Vue from 'vue'
  import TrekkInfo from './TrekkInfo.vue'
  const mountainsState = require('@queries/mountainsState.graphql')

  export default Vue.extend({
    apollo: {
      smountains: {
        loadingKey: 'loading',
        query: mountainsState,
        result( { data: { smountains: { mountains } } }: ApolloQueryResult<any>) {
          this.smountains = mountains
        },
      },
    },
    components: {
      TrekkInfo,
    },
    computed: {
    },
    created() {
      window.navigator.geolocation.getCurrentPosition(
        ({coords: {latitude: lat, longitude: lng}}) => {
          this.center = {lat, lng}
        },
      )
    },
    data(): IMapsInstance {
        return {
          center: {lat: 10, lng: 10},
          infoWinOpen: false,
          selectedMountain: undefined,
          smountains: [] as IMountain[],
        }
    },
    methods: {
      closeInfo(): void {
        this.infoWinOpen = false
      },
      toggleInfoWindow(mountain: IMountain): void {
        if (this.selectedMountain && this.selectedMountain.id === mountain.id) {
          this.infoWinOpen = !this.infoWinOpen
        } else {
          this.selectedMountain = mountain
          this.infoWinOpen = true
        }
      },
    },
    name: 'Maps',
    props: [],
  })
</script>

<style>
</style>