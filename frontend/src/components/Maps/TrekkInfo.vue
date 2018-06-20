<template>
  <gmap-info-window
    v-if="mountain"
    :options="infoOptions"
    :position="{lat: mountain.position.lat, lng: mountain.position.lng}"
    :opened="isOpen"
    @closeclick="infoWinOpen=false"
  >
    <div>{{`${mountain.name}: ${mountain.elevation}m`}}</div>
    <div>{{`${mountain.distance}km away`}}</div>
  </gmap-info-window>
</template>

<script lang="ts">
  interface ITrekkInfo {
    infoOptions: {
      pixelOffset: {
        height: number
        width: number
      }
    }
  }

  import Vue from 'vue'
  import { IPosition } from '@typings/geo'
  export default Vue.extend({
    props: ['onClose', 'mountain', 'isOpen'],
    name: 'TrekkInfo',
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
    computed: {
      position(): IPosition {
        return {
          lat: this.mountain.position.lat,
          lng: this.mountain.position.lng,
        }
      }

    }
  })
</script>

<style>
</style>