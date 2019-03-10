<template>
  <div class="card">
    <img
      v-if="mountain.image"
      class="card-img-top"
      :src="mountain.image.url"
      :alt="$formatMessage({id: 'trekks-filter.mountain-card.image-alt'}, {name: mountain.name})"
    />
    <div class="card-body">
      <h5 class="card-title">{{mountain.name}}, {{mountain.country}}</h5>
      <p class="card-text">🌐 ({{mountain.position.lat}}, {{mountain.position.lng}})</p>
      <p class="card-text">⛰️ {{mountain.elevation}} m</p>
      <p class="card-text">📍 {{mountain.distance}} km away</p>
      <a @click="seeOnMap()" href="#" class="btn btn-primary">See on Map</a>
      <a :href="`/mountain/${mountain.id}`" class="btn btn-primary">Enter</a>
    </div>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  const mapMutation = require('@mutations/mapState.graphql')
  const mountainHintState = require('@mutations/mountainHintState.graphql')

  export default Vue.extend({
    methods: {
      seeOnMap(): void {
        this.$apollo.mutate({
          mutation: mapMutation,
          variables: {
            center: this.mountain.position,
            zoom: 5,
          },
        })
        this.$apollo.mutate({
          mutation: mountainHintState,
          variables: {
            mountain: this.mountain,
          },
        })
      },
    },
    name: 'MountainCard',
    props: ['mountain'],
  })
</script>