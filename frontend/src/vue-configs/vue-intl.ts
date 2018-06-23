import en from '@locales/en.json'
import Vue from 'vue'
import * as VueIntl from 'vue-intl'

Vue.use(VueIntl)

Vue.setLocale('en')

Vue.registerMessages('en', en)
