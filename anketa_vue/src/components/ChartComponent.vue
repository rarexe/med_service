<template>
<v-card width="1200" height="650" class="my-5">
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
  data: () => ({
    data: [],
    layout: {
      margin: { t: 100, r: 100, b: 100, l: 75 },
      title: 'Статистика по разным подразделениям',
      yaxis: {
        title: 'Сумма баллов',
        titlefont: {
          size: 16
        }
      },
      width: 900,
      height: 600
    }
  }
  ),
  methods: {
    getContext () {
      // Получаем список всех анкет
      this.axios.get('//127.0.0.1:8000/anketa/list').then((response) => {
        console.log(response.data)
        this.hospital1 = []
        this.hospital2 = []
        this.hospital1_rel = []
        this.hospital2_rel = []
        this.hospital1_stigma = []
        this.hospital2_stigma = []
        this.hospital1_treat = []
        this.hospital2_treat = []
        this.hospital1_cond = []
        this.hospital2_cond = []
        response.data.forEach(obj => {
          if (obj.hospital === 1) { // Добавляем данные о стационарных подразделениях
            this.hospital1.push(parseInt(obj.result_total))
            this.hospital1_rel.push(parseInt(obj.result_relationship))
            this.hospital1_stigma.push(parseInt(obj.result_stigma))
            this.hospital1_treat.push(parseInt(obj.result_treatment))
            this.hospital1_cond.push(parseInt(obj.result_condition))
            this.hospital1_cond.push(parseInt(obj.result_condition))
          } else { // Добавляем данные об амбулаторных подразделениях
            this.hospital2.push(parseInt(obj.result_total))
            this.hospital2_rel.push(parseInt(obj.result_relationship))
            this.hospital2_stigma.push(parseInt(obj.result_stigma))
            this.hospital2_treat.push(parseInt(obj.result_treatment))
            this.hospital2_cond.push(parseInt(obj.result_condition))
            this.hospital2_cond.push(parseInt(obj.result_condition))
          }
        })
        // Создаем массив для передачи в Plotly
        this.data = [{
          y: this.hospital1,
          boxpoints: 'all',
          type: 'box',
          name: 'Стационарные',
          marker: {
            color: '#4C78A8'
          }
        },
        {
          y: this.hospital2,
          boxpoints: 'all',
          type: 'box',
          name: 'Амбулаторные',
          marker: {
            color: '#72B7B2'
          }
        },
        {
          y: this.hospital1_rel,
          boxpoints: 'all',
          type: 'box',
          name: 'Стационарные (о.)',
          marker: {
            color: '#4C78A8'
          }
        },
        {
          y: this.hospital2_rel,
          boxpoints: 'all',
          type: 'box',
          name: 'Амбулаторные (о.)',
          marker: {
            color: '#72B7B2'
          }
        },
        {
          y: this.hospital1_stigma,
          boxpoints: 'all',
          type: 'box',
          name: 'Стационарные (с.)',
          marker: {
            color: '#4C78A8'
          }
        },
        {
          y: this.hospital2_stigma,
          boxpoints: 'all',
          type: 'box',
          name: 'Амбулаторные (с.)',
          marker: {
            color: '#72B7B2'
          }
        },
        {
          y: this.hospital1_treat,
          boxpoints: 'all',
          type: 'box',
          name: 'Стационарные (л.)',
          marker: {
            color: '#4C78A8'
          }
        },
        {
          y: this.hospital2_treat,
          boxpoints: 'all',
          type: 'box',
          name: 'Амбулаторные (л.)',
          marker: {
            color: '#72B7B2'
          }
        },
        {
          y: this.hospital1_cond,
          boxpoints: 'all',
          type: 'box',
          name: 'Стационарные (б.)',
          marker: {
            color: '#4C78A8'
          }
        },
        {
          y: this.hospital2_cond,
          boxpoints: 'all',
          type: 'box',
          name: 'Амбулаторные (б.)',
          marker: {
            color: '#72B7B2'
          }
        }]
      })
    }
  },
  mounted () {
    this.getContext()
  }
}
</script>
