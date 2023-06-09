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
  data: () => ({
    data: [],
    layout: {
      margin: { b: 100, l: 100 },
      title: 'Cвязь результатов опросника с возрастом респондентов',
      xaxis: {
        title: 'Возраст',
        titlefont: {
          size: 16
        }
      },
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
      this.axios.get('//127.0.0.1:8000/anketa/list').then((response) => {
        console.log(response.data)
        this.ages = []
        this.ages_treat = []
        this.ages_rel = []
        this.ages_stigma = []
        this.ages_total = []
        this.ages_condition = []
        // Создание списка из уникальных возрастов из анкет
        response.data.forEach(obj => {
          if (this.ages.indexOf(obj.age) <= -1) {
            this.ages.push(obj.age)
          }
        })
        // Для каждого возраста считаем средние по субшкалам и суммарному баллу
        for (var i = 0; i < this.ages.length - 1; i++) {
          var scoreTotal = 0
          var scoreTreat = 0
          var scoreStigma = 0
          var scoreRel = 0
          var scoreCond = 0
          var count = 0
          response.data.forEach(obj => {
            if (obj.age === this.ages[i]) {
              scoreTotal += parseInt(obj.result_total)
              scoreStigma += parseInt(obj.result_stigma)
              scoreTreat += parseInt(obj.result_treatment)
              scoreRel += parseInt(obj.result_relationship)
              scoreCond += parseInt(obj.result_condition)
              count += 1
            }
          })
          this.ages_total.push(scoreTotal / count)
          this.ages_rel.push(scoreRel / count)
          this.ages_stigma.push(scoreStigma / count)
          this.ages_treat.push(scoreTreat / count)
          this.ages_condition.push(scoreCond / count)
        }
        this.data = [{
          x: this.ages,
          y: this.ages_total,
          type: 'scatter',
          name: 'Суммарный бал',
          mode: 'markers',
          marker: {
            color: '#4C78A8'
          }
        },
        {
          x: this.ages,
          y: this.ages_rel,
          type: 'scatter',
          name: 'Субшкала отношения',
          mode: 'markers',
          marker: {
            color: '#72B7B2'
          }
        },
        {
          x: this.ages,
          y: this.ages_treat,
          type: 'scatter',
          name: 'Субшкала лечение',
          mode: 'markers',
          marker: {
            color: 'rgb(36,121,108)'
          }
        },
        {
          x: this.ages,
          y: this.ages_stigma,
          type: 'scatter',
          name: 'Субшкала стигма',
          mode: 'markers',
          marker: {
            color: '#0D2A63'
          }
        },
        {
          x: this.ages,
          y: this.ages_condition,
          type: 'scatter',
          name: 'Субшкала бытовые условия',
          mode: 'markers',
          marker: {
            color: '#000000'
          }
        }
        ]
      })
    }
  },
  mounted () {
    this.getContext()
  }
}
</script>
