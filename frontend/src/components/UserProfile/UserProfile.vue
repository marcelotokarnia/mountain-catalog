<template>
  <div class="row h-100">
    <gmap-map
      ref="map"
      :center="{lat: 59.332254, lng: 18.017310}"
      :zoom="5"
      map-type-id="terrain"
      class="col-9 mt-4"
    ></gmap-map>
  </div>
</template>

<script lang="ts">
declare const google: any;
import Vue from "vue";
import { ApolloQueryResult } from "apollo-client";
const UserData = require("@queries/userData.graphql");
export default Vue.extend({
  apollo: {
    user: {
      query: UserData,
      result(result: ApolloQueryResult<{ user: { username: string } | null }>) {
        const {
          data: { user }
        } = result;
        if (!user) {
          window.location.replace("/login");
        }
        this.user = user;
        if (this.$el) {
          this.load_kml();
        }
      }
    }
  },
  data(): { user: { username: string } | null } {
    return {
      user: null
    };
  },
  methods: {
    load_kml() {
      const self: any = this;
      if (self.kml) {
        return;
      }
      self.$refs.map.$mapPromise.then(() => {
        var options = {
          preserveViewport: true,
          clickable: true,
          visibility: "visible",
          url: `http://${window.location.host}/get_strava_kml/${
            self.user!.username
          }/${Math.round(Math.random() * 1000)}`
        };
        self.kml = new google.maps.KmlLayer(options);
        self.kml.setMap(self.$refs.map.$mapObject);
      });
    }
  },
  mounted() {
    if (!this.$apollo.queries.user.loading) {
      this.load_kml();
    }
  },
  name: "UserProfile",
  props: []
});
</script>