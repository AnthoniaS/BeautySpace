import Vue from 'vue'
import VueRouter from 'vue-router'

import BoasVindas from './components/BoasVindas.vue'
import ListaAgendados from './components/ListaAgendados.vue'
import FormLogin from './components/FormLogin.vue'
import Agendamento from "./components/Agendamento"

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    routes: [
        { path: '/', component: BoasVindas },
        { path: '/agendados', component: ListaAgendados },
        { path: '/login', component: FormLogin },
        { path: '/agendamentos', component: Agendamento },


    ]
})