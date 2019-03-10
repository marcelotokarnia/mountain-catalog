<template>
  <gmap-info-window
    v-if="mountain"
    :options="infoOptions"
    :position="position"
    :opened="true"
    @closeclick="onClose"
  >
    <div v-html="$formatMessage({id: 'maps.trekk-info.name-elevation'}, {
      elevation: mountain.elevation,
      name: mountain.name,
    })" />
    <div v-html="$formatMessage({id: 'maps.trekk-info.distance'}, {
      distance: mountain.distance
    })" />
    <img v-if="mountain.image" :src="mountain.image.url" />
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
  const mountainHintMutation = require('@mutations/mountainHintState.graphql')

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
    methods: {
      onClose(): void {
        this.$apollo.mutate({
          mutation: mountainHintMutation,
          variables: {
            mountain: null,
          },
        })
      },
    },
    name: 'TrekkInfo',
    props: ['mountain'],
  })
</script>