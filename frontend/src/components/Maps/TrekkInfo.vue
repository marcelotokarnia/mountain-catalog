<template>
  <gmap-info-window
    v-if="mountain"
    :options="infoOptions"
    :position="{lat: mountain.position.lat, lng: mountain.position.lng}"
    :opened="isOpen"
    @closeclick="infoWinOpen=false"
  >
    <div v-html="$formatMessage({id: 'maps.trekk-info.name-elevation'}, {
      elevation: mountain.elevation,
      name: mountain.name,
    })" />
    <div v-html="$formatMessage({id: 'maps.trekk-info.distance'}, {
      distance: mountain.distance
    })" />
    <img v-if="mountain.image" v-bind:src="mountain.image" />
  </gmap-info-window>
</template>

<script lang="ts">
  interface ITrekkInfo {
    infoOptions: {
      pixelOffset: {
        height: number
        width: number,
      },
    }
  }

  import { IPosition } from '@typings/geo'
  import Vue from 'vue'
  export default Vue.extend({
    computed: {
      position(): IPosition {
        return {
          lat: this.mountain.position.lat,
          lng: this.mountain.position.lng,
        }
      },
    },
    data(): ITrekkInfo {
      return {
        infoOptions: {
          pixelOffset: {
            height: -35,
            width: 0,
          },
        },
      }
    },
    name: 'TrekkInfo',
    props: ['onClose', 'mountain', 'isOpen'],
  })
</script>

<style>
</style>