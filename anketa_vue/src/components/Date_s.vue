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
  dates: [],
  dates_new: [],
  data: () => ({
    data: [],
    layout: {
      margin: { t: 100, r: 50, b: 100, l: 75 },
      title: 'Статистика по дате заполнения для амбулаторного подразделения (стигма)',
      width: 900,
      height: 600,
      yaxis: {
        title: 'Сумма баллов',
        titlefont: {
          size: 14
        }
      },
      xaxis: {
        title: 'Дата заполнения анкеты',
        titlefont: {
          size: 14
        }
      }
    }
  }
  ),
  methods: {
    getContext () {
      this.data = []
      this.dates_new = []
      this.dates = []
      this.axios.get('//127.0.0.1:8000/anketa/list').then((response) => {
        console.log(response.data)
        // Создаем массив с уникальными датами из анкет
        response.data.forEach(obj => {
          if (this.dates.includes(obj.data_time.substring(0, 7)) === false) {
            this.dates.push(obj.data_time.substring(0, 7)) // В data_time содержится информация о времени, для графика берем только дату
          }
        })
      })
      this.dep = []
      this.axios.get('//127.0.0.1:8000/anketa/list').then((response) => {
        console.log(response.data)
        // Для каждой уникальной даты добавляем значение по субшкале
        for (var i = 0; i < this.dates.length; i++) {
          response.data.forEach(obj => {
            if (obj.data_time.substring(0, 7) === this.dates[i] && obj.hospital === 2) {
              this.dep.push(parseInt(obj.result_stigma))
            }
          })
          this.data.push({
            y: this.dep,
            boxpoints: 'all',
            type: 'box',
            name: this.dates[i],
            marker: {
              color: '#0D2A63'
            }
          })
          this.dep = []
        }
      })
    }
  },
  mounted () {
    this.getContext()
  }
}
</script>
