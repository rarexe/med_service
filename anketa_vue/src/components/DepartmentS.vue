<template>
<v-card width="1200" height="600" class="my-5">
<Plotly :data="data" :layout="layout" :displayModeBar="true"></Plotly>
</v-card>
</template>

<script>
import { Plotly } from 'vue-plotly'
export default {
  components: {
    Plotly
  },
  name: 'Chart',
  departments: Object,
  data: () => ({
    data: [],
    layout: {
      margin: { t: 100, r: 50, b: 150, l: 75 },
      title: 'Статистика отделений для стационарного подразделения',
      width: 900,
      height: 600,
      yaxis: {
        title: 'Сумма баллов',
        titlefont: {
          size: 16
        }
      }
    }
  }
  ),
  methods: {
    getContext () {
      this.data = []
      this.departments = []
      this.axios.get('//127.0.0.1:8000/department/').then((response) => {
        console.log(response.data)
        this.departments = response.data
      })
      this.dep = []
      this.axios.get('//127.0.0.1:8000/anketa/list').then((response) => {
        console.log(response.data)
        for (var i = 0; i < this.departments.length; i++) {
          response.data.forEach(obj => {
            if (obj.department === this.departments[i].id && this.departments[i].hospital_department === 1) {
              this.dep.push(parseInt(obj.result_total))
            }
          })
          this.data.push({
            y: this.dep,
            boxpoints: 'all',
            type: 'box',
            name: this.departments[i].department_name.replace(' стационарное психиатрическое', ''),
            legendgroup: 'group1',
            marker: {
              color: '#4C78A8'
            }
          })
          this.dep = []
        }
      })
      this.dep_rel = []
      this.axios.get('//127.0.0.1:8000/anketa/list').then((response) => {
        console.log(response.data)
        for (var i = 0; i < this.departments.length; i++) {
          response.data.forEach(obj => {
            if (obj.department === this.departments[i].id && this.departments[i].hospital_department === 1) {
              this.dep_rel.push(parseInt(obj.result_relationship))
            }
          })
          this.data.push({
            y: this.dep_rel,
            boxpoints: 'all',
            type: 'box',
            name: this.departments[i].department_name.replace(' стационарное психиатрическое', '') + ' (о.)',
            legendgroup: 'group2',
            marker: {
              color: '#72B7B2'
            }
          })
          this.dep_rel = []
        }
      })
      this.dep_stigma = []
      this.axios.get('//127.0.0.1:8000/anketa/list').then((response) => {
        console.log(response.data)
        for (var i = 0; i < this.departments.length; i++) {
          response.data.forEach(obj => {
            if (obj.department === this.departments[i].id && this.departments[i].hospital_department === 1) {
              this.dep_stigma.push(parseInt(obj.result_stigma))
            }
          })
          this.data.push({
            y: this.dep_stigma,
            boxpoints: 'all',
            type: 'box',
            name: this.departments[i].department_name.replace(' стационарное психиатрическое', '') + ' (с.)',
            legendgroup: 'group3',
            marker: {
              color: 'rgb(36,121,108)'
            }
          })
          this.dep_stigma = []
        }
      })
      this.dep_treat = []
      this.axios.get('//127.0.0.1:8000/anketa/list').then((response) => {
        console.log(response.data)
        for (var i = 0; i < this.departments.length; i++) {
          response.data.forEach(obj => {
            if (obj.department === this.departments[i].id && this.departments[i].hospital_department === 1) {
              this.dep_treat.push(parseInt(obj.result_treatment))
            }
          })
          this.data.push({
            y: this.dep_treat,
            boxpoints: 'all',
            type: 'box',
            name: this.departments[i].department_name.replace(' стационарное психиатрическое', '') + ' (л.)',
            legendgroup: 'group4',
            marker: {
              color: '#0D2A63'
            }
          })
          this.dep_treat = []
        }
      })
      this.dep_condition = []
      this.axios.get('//127.0.0.1:8000/anketa/list').then((response) => {
        console.log(response.data)
        for (var i = 0; i < this.departments.length; i++) {
          response.data.forEach(obj => {
            if (obj.department === this.departments[i].id && this.departments[i].hospital_department === 1) {
              this.dep_condition.push(parseInt(obj.result_condition))
            }
          })
          this.data.push({
            y: this.dep_condition,
            boxpoints: 'all',
            type: 'box',
            name: this.departments[i].department_name.replace(' стационарное психиатрическое', '') + ' (б.)',
            legendgroup: 'group5',
            marker: {
              color: '#000000'
            }
          })
          this.dep_condition = []
        }
      })
    }
  },
  mounted () {
    this.getContext()
  }
}
</script>
