<template>
  <div>
    {{$formatMessage({id: 'profile.profile.profile'})}}
    {{user ? user.username : ''}}
    <div class="row maps-main" style="height: 500px;">
      <gmap-map
        ref="map"
        :center="{lat: 59.332254, lng: 18.017310}"
        :zoom="5"
        map-type-id="terrain"
        class="col-9 h-100"
      >
      </gmap-map>
    </div>
  </div>
</template>

<script lang="ts">
declare const google: any
import Vue from 'vue'
import { ApolloQueryResult } from 'apollo-client'
const UserData = require('@queries/userData.graphql')
export default Vue.extend({
  apollo: {
    user: {
      query: UserData,
      result( result: ApolloQueryResult<{ user: { username: string} | null }>) {
        const { data: { user } } = result
        if (!user) {
          window.location.replace('/login')
        }
        this.user = user
        const self: any = this;
        self.$refs.map.$mapPromise.then(
        () => {
            var options = {
              preserveViewport: true, 
              clickable: true,
              visibility: "visible",
              url: `https://${window.location.host}/get_strava_kml/${this.user!.username}`
            };
            self.kml = new google.maps.KmlLayer(options);
            self.kml.setMap(self.$refs.map.$mapObject)
        })
      },
    },
  },
  data() : {user: {username: string} | null} {
    return {
      user: null
    }
  },
  methods: {

  },
  name: 'UserProfile',
  props: [],
})
</script>