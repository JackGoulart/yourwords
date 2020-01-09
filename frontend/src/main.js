import Vue from 'vue'
import App from './App.vue'
import VueRouter from 'vue-router'
import {routes} from './routes'

import Vuetify from 'vuetify'
import 'vuetify/dist/vuetify.min.css' 


Vue.config.productionTip = false
Vue.use(VueRouter)
Vue.use(Vuetify)

const router = new VueRouter({
  routes : routes,
  mode : 'history'
})

new Vue({
  router,
  render: h => h(App),
}).$mount('#app')
