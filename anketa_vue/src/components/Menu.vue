<template>
  <v-container>
    <v-row class="mt-5" >
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64" rounded="lg">
          <v-list-item link :href="'/graphics'">
            <v-list-item-title>Статистика по разным подразделениям</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64" rounded="lg">
          <v-list-group :value="false">
            <template v-slot:activator>
              <v-list-item-title>Статистика по разным датам в пределах одного подразделения</v-list-item-title>
            </template>
            <v-list-group :value="false" no-action sub-group>
            <template v-slot:activator>
              <v-list-item-title>Стационарное подразделение</v-list-item-title>
            </template>
              <v-list-item link :href="'/date_s'">
                <v-list-item-title>Суммарный балл</v-list-item-title>
              </v-list-item>
              <v-list-item link :href="'/dateS_r'">
                <v-list-item-title>Субшкала отношения</v-list-item-title>
              </v-list-item>
              <v-list-item link :href="'/dateS_t'">
                <v-list-item-title>Субшкала лечение</v-list-item-title>
              </v-list-item>
              <v-list-item link :href="'/dateS_s'">
                <v-list-item-title>Субшкала стигма</v-list-item-title>
              </v-list-item>
              <v-list-item link :href="'/dateS_c'">
                <v-list-item-title>Субшкала бытовые условия</v-list-item-title>
              </v-list-item>
            </v-list-group>
            <v-list-group :value="false" no-action sub-group>
            <template v-slot:activator>
              <v-list-item-title>Амбулаторне подразделение</v-list-item-title>
            </template>
              <v-list-item link :href="'/date_a'">
                <v-list-item-title>Суммарный балл</v-list-item-title>
              </v-list-item>
              <v-list-item link :href="'/datA_r'">
                <v-list-item-title>Субшкала отношения</v-list-item-title>
              </v-list-item>
              <v-list-item link :href="'/datA_t'">
                <v-list-item-title>Субшкала лечение</v-list-item-title>
              </v-list-item>
              <v-list-item link :href="'/dateA_s'">
                <v-list-item-title>Субшкала стигма</v-list-item-title>
              </v-list-item>
               <v-list-item link :href="'/dateA_c'">
                <v-list-item-title>Субшкала бытовые условия</v-list-item-title>
              </v-list-item>
            </v-list-group>
          </v-list-group>
        </v-list>
      </v-col>
    </v-row>
    <v-row>
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64" rounded="lg">
          <v-list-group :value="false">
            <template v-slot:activator>
              <v-list-item-title>Статистика по разным врачам одного подразделения</v-list-item-title>
            </template>
            <v-list-item link :href="'/doctor_s'">
              <v-list-item-title>Стационарное подразделение</v-list-item-title
              >
            </v-list-item>
            <v-list-item link :href="'/doctor_a'">
              <v-list-item-title>Амбулаторное подразделение</v-list-item-title
              >
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-col>
    </v-row>
       <v-row>
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64" rounded="lg">
          <v-list-group :value="false">
            <template v-slot:activator>
              <v-list-item-title>Статистика по разным отделениям одного подразделения</v-list-item-title>
            </template>
            <v-list-item link :href="'/department_s'">
              <v-list-item-title>Стационарное подразделение</v-list-item-title
              >
            </v-list-item>
            <v-list-item link :href="'/department_a'">
              <v-list-item-title>Амбулаторное подразделение</v-list-item-title
              >
            </v-list-item>
          </v-list-group>
        </v-list>
      </v-col>
    </v-row>
       <v-row class="mt-5">
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64" rounded="lg">
          <v-list-item link :href="'/scatter'">
            <v-list-item-title>Cвязь результатов опросника с возрастом респондентов</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64" rounded="lg">
          <v-list-item @click="getModel">
            <v-list-item-title>Скачать файл с анкетами</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
      <v-col cols="9" class="mx-auto">
        <v-list dark color="#455A64" rounded="lg">
          <v-list-item @click="getFakeModel">
            <v-list-item-title>Скачать файл с непрошедшими проверку анкетами</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-col>
    </v-row>
  </v-container>
</template>
<script>
export default {
  methods:
  {
    getModel () {
      this.axios.get('//127.0.0.1:8000/anketa-xlsx/', { responseType: 'blob' })
        .then(response => {
          const url = window.URL.createObjectURL(new Blob([response.data]))
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', 'anketa.xlsx')
          document.body.appendChild(link)
          link.click()
        })
        .catch(error => {
          console.log(error)
        })
    },
    getFakeModel () {
      this.axios.get('//127.0.0.1:8000/fake_anketa-xlsx/', { responseType: 'blob' })
        .then(response => {
          const url = window.URL.createObjectURL(new Blob([response.data]))
          const link = document.createElement('a')
          link.href = url
          link.setAttribute('download', 'fake_anketa.xlsx')
          document.body.appendChild(link)
          link.click()
        })
        .catch(error => {
          console.log(error)
        })
    }
  }
}
</script>
