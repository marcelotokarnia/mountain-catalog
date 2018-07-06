<template>
  <div class="row maps-main">
    <gmap-map
      :center="center"
      :zoom="zoom"
      map-type-id="terrain"
      class="col-9"
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
    <TrekksFilter class="col-3 pre-scrollable scrollable-view" />
  </div>
</template>

<script lang='ts'>
  interface IMapsInstance {
    center?: IPosition
    zoom?: number
    smountains: IMountain[]
    selectedMountain?: IMountain
    infoWinOpen: boolean
  }

  import { IPosition } from '@typings/geo'
  import { IMap } from '@typings/map'
  import { IDataMountains, IMountain } from '@typings/mountains'
  import TrekksFilter from '@components/TrekksFilter'
  import { ApolloQueryResult } from 'apollo-client'
  import gql from 'graphql-tag'
  import * as R from 'ramda'
  import Vue from 'vue'
  import TrekkInfo from './TrekkInfo.vue'
  const mountainsState = require('@queries/mountainsState.graphql')
  const mapState = require('@queries/mapState.graphql')
  const mapMutation = require('@mutations/mapState.graphql')

  export default Vue.extend({
    apollo: {
      smap: {
        query: mapState,
        result( result: ApolloQueryResult<{ smap: IMap }>) {
          const { data: { smap: { center, zoom } } } = result
          this.center = center
          this.zoom = zoom
        },
      },
      smountains: {
        query: mountainsState,
        result( { data: { smountains: { mountains } } }: ApolloQueryResult<{smountains: { mountains: IMountain[] } }>) {
          this.smountains = mountains
        },
      },
    },
    components: {
      TrekkInfo,
      TrekksFilter,
    },
    computed: {
    },
    created() {
      window.navigator.geolocation.getCurrentPosition(
        ({coords: {latitude: lat, longitude: lng}}) => {
          this.$apollo.mutate({
            mutation: mapMutation,
            variables: {
              center: {lat, lng},
              zoom: 5
            },
          })
        },
      )
    },
    data(): IMapsInstance {
        return {
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

<style lang="stylus" scoped>
  .maps-main
    height 100%
  .scrollable-view
    max-height 100%
</style>