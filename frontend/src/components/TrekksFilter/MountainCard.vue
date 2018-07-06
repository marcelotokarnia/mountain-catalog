<template>
  <div class="card">
    <img
      v-if="mountain.image"
      class="card-img-top"
      :src="mountain.image"
      :alt="$formatMessage({id: 'trekks-filter.mountain-card.image-alt'}, {name: mountain.name})"
    />
    <div class="card-body">
      <h5 class="card-title">{{mountain.name}}, {{mountain.country}}</h5>
      <p class="card-text">🌐 ({{mountain.position.lat}}, {{mountain.position.lng}})</p>
      <p class="card-text">⛰️ {{mountain.elevation}} m</p>
      <p class="card-text">📍 {{mountain.distance}} km away</p>
      <a href="#" class="btn btn-primary">See on Map</a>
      <a href="#" class="btn btn-primary">Enter</a>
    </div>
  </div>
</template>

<script lang="ts">
  import Vue from 'vue'
  export default Vue.extend({
    name: 'MountainCard',
    props: ["mountain"],
    methods: {
      seeOnMap(): void {

      }
    }
  })
</script>