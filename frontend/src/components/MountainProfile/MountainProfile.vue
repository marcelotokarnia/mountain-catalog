<template>
  <div>
    <div v-if="loading">LOADING</div>
    <div v-if="!loading && mountain">
      <div>
        <img v-if="mountain.image" :src="mountain.image.url">
        <p v-html="`${mountain.name} - ${mountain.elevation}m`" />
      </div>
      <div>
        <p v-html="$formatMessage({id: 'mountain-profile.distance'}, {
          distance: mountain.distance
        })" />
      </div>
      <div>
        <p v-html="$formatMessage({id: 'mountain-profile.position'}, {
          country: mountain.country,
          lat: mountain.position.lat,
          lng: mountain.position.lng,
        })" />
        <p v-html="`${mountain.region}, ${mountain.state}, ${mountain.province}`" />
      </div>
      <div v-if="mountain.curiosities">
        <p v-for="(curi, idx) in mountain.curiosities.split('\n')" :key="idx" v-html="curi" />
      </div>
      <div v-html="$formatMessage({id: 'mountain-profile.created_by'}, {
        createdBy: mountain.createdBy
      })" />
      <div v-if="mountain.image">
        <hr/>
        <div v-html="$formatMessage({id: 'mountain-profile.image'})" />
        <h2>{{mountain.image.title}}</h2>
        <div>{{mountain.image.url}}</div>
        <div>{{mountain.image.votes}}</div>
        <div>{{mountain.image.createdBy}}</div>
      </div>
      <div v-if="mountain.text">
        <hr/>
        <div v-html="$formatMessage({id: 'mountain-profile.text'})" />
        <h2>{{mountain.text.title}}</h2>
        <div>{{mountain.text.record}}</div>
        <div>{{mountain.text.votes}}</div>
        <div>{{mountain.text.createdBy}}</div>
      </div>
      <div v-if="mountain.video">
        <hr/>
        <div v-html="$formatMessage({id: 'mountain-profile.video'})" />
        <a :href="mountain.video.link">{{mountain.video.provider}}</a>
        <div>{{mountain.video.votes}}</div>
        <div>{{mountain.video.createdBy}}</div>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
interface IMountainProfile {
  loading: boolean
  mountain?: IMountain
  position?: IPosition
}

import { IPosition } from '@typings/geo'
import { IMountain } from '@typings/mountains'
import { ApolloQueryResult } from 'apollo-client'
import Vue from 'vue'
const mountainQuery = require('@queries/mountain.graphql')
const mePositionQuery = require('@queries/mePositionState.graphql')

export default Vue.extend({
  apollo: {
    mountain: {
      query: mountainQuery,
      watchLoading(isLoading) {
        this.loading = isLoading
      },
      skip() {
        return true
      },
    },
    smePosition: {
      query: mePositionQuery,
        result({data: {smePosition: { position: {lat, lng} } } }:
          ApolloQueryResult<{smePosition: { position: IPosition } }>) {
            this.position = {lat, lng}
            this.$apollo.queries.mountain.refetch({
              id: this.$route.params.id,
              position: this.position,
            })
            this.$apollo.queries.mountain.skip = false
        },
    },
  },
  data(): IMountainProfile {
    return {
      loading: true,
      mountain: undefined,
      position: undefined,
    }
  },
  methods: {

  },
  name: 'MountainProfile',
  props: ['params'],
})
</script>