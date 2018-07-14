<template>
  <div class="row maps-main">
    <gmap-map
      :center="center"
      :zoom="zoom"
      map-type-id="terrain"
      class="col-9"
    >
      <TrekkInfo :mountain="selectedMountain" />
      <gmap-marker
        v-if="me"
        icon="/static/icons/bluedot.png"
        :position="me"
      />
      <gmap-marker
        :icon="`/static/icons/${getMountainIcon(m)}.png`"
        :key="m.id"
        v-for="m in smountains"
        :position="m.position"
        :clickable="true"
        :draggable="false"
        @click="toggleInfoWindow(m)"
      />
    </gmap-map>
    <TrekksFilter ref="trekksFilter" class="col-3 pre-scrollable scrollable-view" />
  </div>
</template>

<script lang='ts'>
  interface IMapsInstance {
    me?: IPosition
    center?: IPosition
    zoom?: number
    smountains: IMountain[]
    selectedMountain?: IMountain
    infoWinOpen: boolean
  }

  import TrekksFilter from '@components/TrekksFilter'
  import { IPosition } from '@typings/geo'
  import { IMap } from '@typings/map'
  import { IDataMountains, IMountain } from '@typings/mountains'
  import { ApolloQueryResult } from 'apollo-client'
  import gql from 'graphql-tag'
  import * as R from 'ramda'
  import Vue from 'vue'
  import TrekkInfo from './TrekkInfo.vue'
  const mountainsState = require('@queries/mountainsState.graphql')
  const mountainHintState = require('@queries/mountainHintState.graphql')
  const mapState = require('@queries/mapState.graphql')
  const mapMutation = require('@mutations/mapState.graphql')
  const mountainHintMutation = require('@mutations/mountainHintState.graphql')
  const mePositionMutation = require('@mutations/mePositionState.graphql')

  const scrollIntoView = (mountainId: number, mapsComponent: Vue) => {
    const el = R.path(
      ['$refs', 'trekksFilter', '$refs', `mountainCard${mountainId}`, 0, '$el'],
    )(mapsComponent) as Element
    el.scrollIntoView()
  }

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
      smountainHint: {
        query: mountainHintState,
        result( { data: { smountainHint: { mountain } } }:
          ApolloQueryResult<{smountainHint: { mountain: IMountain } }>) {
          this.selectedMountain = mountain
        },
      },
      smountains: {
        query: mountainsState,
        result( { data: { smountains: { mountains } } }:
          ApolloQueryResult<{smountains: { mountains: IMountain[] } }>) {
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
          this.me = {lat, lng}
          this.$apollo.mutate({
            mutation: mapMutation,
            variables: {
              center: {lat, lng},
              zoom: 5,
            },
          })
          this.$apollo.mutate({
            mutation: mePositionMutation,
            variables: {
              position: {lat, lng},
            },
          })
        },
      )
    },
    data(): IMapsInstance {
        return {
          center: undefined,
          infoWinOpen: false,
          me: undefined,
          selectedMountain: undefined,
          smountains: [] as IMountain[],
          zoom: undefined,
        }
    },
    methods: {
      getMountainIcon(mountain: IMountain): string {
        return mountain.elevation > 5000 ?
          'mountainred' :
          mountain.elevation > 3000 ?
            'mountainyellow' :
            'mountaingreen'
      },
      toggleInfoWindow(mountain: IMountain): void {
        if (R.equals(mountain.id, R.path(['id'], this.selectedMountain))) {
          this.$apollo.mutate({
            mutation: mountainHintMutation,
            variables: {
              mountain: null,
            },
          })
        } else {
          this.$apollo.mutate({
            mutation: mountainHintMutation,
            variables: {
              mountain,
            },
          })
          scrollIntoView(mountain.id, this)
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