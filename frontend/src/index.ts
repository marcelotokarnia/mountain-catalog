import App from '@components/App.vue'
import Vue from 'vue'

import apolloProvider from '@src/vue-configs/vue-apollo'
import '@src/vue-configs/vue-intl'
import router from '@src/vue-configs/vue-router'
import '@src/vue-configs/vue2-google-maps'

const v = new Vue({
    components: {
        App,
    },
    el: '#app',
    provide: apolloProvider.provide(),
    router,
    template: `<App />`,
})
