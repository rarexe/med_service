import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Login from '../components/Login.vue'
import ChartComponent from '../components/ChartComponent.vue'
import Menu from '../components/Menu.vue'
import DepartmentS from '../components/DepartmentS.vue'
import DepartmentA from '../components/DepartmentA.vue'
import DoctorA from '../components/DoctorsA.vue'
import DoctorS from '../components/DoctorsS.vue'
import Scatter from '../components/Scatter.vue'
import DateA from '../components/DateA.vue'
import DateAS from '../components/Date_s.vue'
import DateAR from '../components/DateA_r.vue'
import DateAT from '../components/DateA_t.vue'
import DateS from '../components/DateS.vue'
import DateSS from '../components/DateS_s.vue'
import DateSR from '../components/DateS_r.vue'
import DateST from '../components/DateS_t.vue'
import DateAC from '../components/DateA_c.vue'
import DateSC from '../components/DateS_c.vue'
Vue.use(VueRouter)

const routes = [
  {
    path: '/anketa',
    name: 'Anketa',
    component: Home
  },
  {
    path: '/account',
    component: Login
  },
  {
    path: '/graphics',
    component: ChartComponent
  },
  {
    path: '/menu',
    component: Menu
  },
  {
    path: '/department_s',
    component: DepartmentS
  },
  {
    path: '/department_a',
    component: DepartmentA
  },
  {
    path: '/doctor_a',
    component: DoctorA
  },
  {
    path: '/doctor_s',
    component: DoctorS
  },
  {
    path: '/scatter',
    component: Scatter
  },
  {
    path: '/date_a',
    component: DateA
  },
  {
    path: '/dateA_s',
    component: DateAS
  },
  {
    path: '/datA_t',
    component: DateAT
  },
  {
    path: '/datA_r',
    component: DateAR
  },
  {
    path: '/date_s',
    component: DateS
  },
  {
    path: '/dateS_s',
    component: DateSS
  },
  {
    path: '/dateS_t',
    component: DateST
  },
  {
    path: '/dateS_r',
    component: DateSR
  },
  {
    path: '/dateS_c',
    component: DateSC
  },
  {
    path: '/dateA_c',
    component: DateAC
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
