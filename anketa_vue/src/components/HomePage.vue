<template>
  <v-form class="mb-footer">
    <v-container >
      <v-card class="my-5">
        <v-card-title>Анкета</v-card-title>
        <v-col>
          <v-text-field
            v-model="anketa.personal_number"
            label="Номер амбулаторной карты"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-select
            v-model="anketa.hospital"
            :items="hospitals"
            item-value="id"
            item-text="hospital_name"
            outlined
            label="Медицинское учреждение"
            @change="updateContext"
          ></v-select>
        </v-col>
        <v-col>
          <v-select
              v-model="anketa.department"
              :items="departments_names"
              item-value="id"
              item-text="department_name"
              outlined
              label="Отделение"
              @change="updateContext"
            ></v-select>
        </v-col>
        <v-col>
          <v-select
            v-model="anketa.doctor"
            :items="doctors_names"
            item-value="id"
            item-text="doctor_name"
            label="Доктор"
            @change="updateContext"
            outlined
          ></v-select>
        </v-col>
        <v-col>
          <v-text-field
            v-model="anketa.age"
            label="Возраст"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-select
          v-model="anketa.gender"
          label="Пол"
          :items="['Женский', 'Мужской']"
          outlined
          ></v-select>
        </v-col>
        <div>
        <v-card-title>Проставьте цифры от 0 до 3 (0 - неверно, 1 - частично  неверно, 2 - частично верно, 3 - верно).</v-card-title>
        </div>
        <v-col>
          <v-card-subtitle>1. Я доволен (довольна) результатами проводимого лечения.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q1"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>2. Мне не помогают лекарства которыми меня лечат.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q2"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>3. Результаты лечения не такие, как я ожидал (ожидала).</v-card-subtitle>
          <v-text-field
            v-model="anketa.q3"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>4. У лекарств, которыми меня лечат, непереносимые побочные эффекты.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q4"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>5. В результате лечения у меня улучшается самочувствие.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q5"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>6. В ходе лечения у меня не улучшается состояние.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q6"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>7. Лечение дает мне бодрость и активность.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q7"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>8. Расписание работы врачей вызывает неудобство.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q8"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>9. В будущем в случае необходимости я буду обращаться за помощью к психиатрам.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q9"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>10. Меня привлекают к обсуждению плана моего лечения.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q10"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>11. Очереди на прием к врачу слишком длинные.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q11"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>12. Выздоровление зависит, прежде всего, от лечения, а не от воли Бога.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q12"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>13. Лечение помогает мне не бояться жизненных трудностей.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q13"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>14. Болезнь прошла сама по себе, доктор здесь ни при чем.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q14"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>15. Лечение помогает мне лучше понимать себя и других людей.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q15"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>16. Мне хочется продолжить начатый курс лечения.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q16"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>17. Я хочу постоянно наблюдаться у моего лечащего врача.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q17"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>18. В ходе лечения я смог(ла) увидеть мои недостатки, осложняющие мне жизнь.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q18"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>19. Мне трудно попасть к врачу из-за проблем с транспортом.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q19"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>20. Лечение не помогает мне легче общаться с окружающими.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q20"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>21. Получение льготных рецептов не вызывает проблем.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q21"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>22. Меня надо лечить именно так, как это делал мой лечащий врач.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q22"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>23. Лечение помогает мне лучше решать свои проблемы.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q23"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>24. Лекарства, которые мне выписывают слишком дороги.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q24"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>25. Мой лечащий врач не может четко и понятно ответить на мои вопросы.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q25"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>26. Лечение не помогает мне с оптимизмом смотреть в будущее.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q26"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>27. Моего врача интересуют только мои симптомы, как человек я ему был неинтересен.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q27"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>28. Необходимость лечиться у психиатра мешает моим жизненным планам.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q28"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>29. Мне трудно помнить дату и время посещения врача.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q29"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>30. Лечащий врач помогает мне уточнить планы на будущее.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q30"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>31. Меня угнетают контакты с больными, посещающими диспансер.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q31"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>32. Я могу рассказать лечащему врачу события из своей личной жизни, даже если они непосредственно не относились к лечению.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q32"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>33. Я боюсь, что окружающие узнают, что я лечусь у психиатра.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q33"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>34. При посещении диспансера я получаю важную для себя информацию (Информация, представленная в диспансере интересна и полезна).</v-card-subtitle>
          <v-text-field
            v-model="anketa.q34"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>35. Мой лечащий врач не может понять, что мне нужно.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q35"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>36. Я опасаюсь, что прием психотропных препаратов ухудшит отношение ко мне окружающих.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q36"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>37. Медицинский персонал в диспансере достаточно внимательный и чуткий.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q37"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>38. С лечащим врачом у меня нет хорошего эмоционального контакта.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q38"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>39. Мой лечащий врач достаточно знающий и компетентный.</v-card-subtitle>
          <v-text-field
            v-model="anketa.q39"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-card-subtitle>40. Мой лечащий врач не уделял мне достаточно внимания и времени. </v-card-subtitle>
          <v-text-field
            v-model="anketa.q40"
            required
            outlined
            type="number"
          ></v-text-field>
        </v-col>
        <v-col>
          <v-btn large color="blue-grey darken-2"  class="text-center my-5 mr-5 white--text" @click="postAnketa">
            Отправить
          </v-btn>
        </v-col>
      </v-card>
    </v-container>
  </v-form>
</template>
<script>
export default {
  name: 'Anketa',
  data: () => ({
    check_anketa: [],
    hospitals: Object,
    hospital_names: [],
    departments: Object,
    departments_names: [],
    doctors: Object,
    doctors_names: [],
    anketa: {
      personal_number: '',
      hospital: '',
      department: '',
      doctor: '',
      age: '',
      gender: '',
      q1: '',
      q2: '',
      q3: '',
      q4: '',
      q5: '',
      q6: '',
      q7: '',
      q8: '',
      q9: '',
      q10: '',
      q11: '',
      q12: '',
      q13: '',
      q14: '',
      q15: '',
      q16: '',
      q17: '',
      q18: '',
      q19: '',
      q20: '',
      q21: '',
      q22: '',
      q23: '',
      q24: '',
      q25: '',
      q26: '',
      q27: '',
      q28: '',
      q29: '',
      q30: '',
      q31: '',
      q32: '',
      q33: '',
      q34: '',
      q35: '',
      q36: '',
      q37: '',
      q38: '',
      q39: '',
      q40: '',
      result_treatment: '',
      result_relationship: '',
      result_stigma: '',
      result_total: '',
      result_condition: ''
    }
  }),
  methods: {
    getContext () {
      this.axios.get('//127.0.0.1:8000/hospital/').then((response) => {
        console.log(response.data)
        this.hospitals = response.data
      })
      this.axios.get('//127.0.0.1:8000/department/').then((response) => {
        console.log(response.data)
        this.departments = response.data
      })
      this.axios.get('//127.0.0.1:8000/doctor/').then((response) => {
        console.log(response.data)
        this.doctors = response.data
      })
    },
    postAnketa () {
      console.log(this.anketa)
      this.anketa.result_treatment = parseInt(this.anketa.q1) + parseInt(this.anketa.q5) + parseInt(this.anketa.q7) + parseInt(this.anketa.q12) + parseInt(this.anketa.q13) + parseInt(this.anketa.q15) + parseInt(this.anketa.q16) + parseInt(this.anketa.q18) + parseInt(this.anketa.q23) + (18 - (parseInt(this.anketa.q2) + parseInt(this.anketa.q3) + parseInt(this.anketa.q4) + parseInt(this.anketa.q6) + parseInt(this.anketa.q20) + parseInt(this.anketa.q26)))
      this.anketa.result_relationship = parseInt(this.anketa.q9) + parseInt(this.anketa.q22) + parseInt(this.anketa.q30) + parseInt(this.anketa.q32) + parseInt(this.anketa.q39) + (21 - (parseInt(this.anketa.q14) + parseInt(this.anketa.q17) + parseInt(this.anketa.q25) + parseInt(this.anketa.q27) + parseInt(this.anketa.q35) + parseInt(this.anketa.q38) + parseInt(this.anketa.q40)))
      this.anketa.result_stigma = parseInt(this.anketa.q33) + (6 - (parseInt(this.anketa.q28) + parseInt(this.anketa.q36)))
      this.anketa.result_condition = parseInt(this.anketa.q10) + parseInt(this.anketa.q19) + parseInt(this.anketa.q24) + parseInt(this.anketa.q31) + parseInt(this.anketa.q37) + (15 - (parseInt(this.anketa.q8) + parseInt(this.anketa.q11) + parseInt(this.anketa.q21) + parseInt(this.anketa.q29) + parseInt(this.anketa.q34)))
      this.anketa.result_total = this.anketa.result_treatment + this.anketa.result_relationship + this.anketa.result_stigma + this.anketa.result_condition
      this.check_anketa.push(parseInt(this.anketa.q1), parseInt(this.anketa.q2), parseInt(this.anketa.q3), parseInt(this.anketa.q4), parseInt(this.anketa.q5), parseInt(this.anketa.q6), parseInt(this.anketa.q7), parseInt(this.anketa.q8), parseInt(this.anketa.q9), parseInt(this.anketa.q10), parseInt(this.anketa.q11), parseInt(this.anketa.q12), parseInt(this.anketa.q13), parseInt(this.anketa.q14), parseInt(this.anketa.q15), parseInt(this.anketa.q16), parseInt(this.anketa.q17), parseInt(this.anketa.q18), parseInt(this.anketa.q19), parseInt(this.anketa.q20), parseInt(this.anketa.q21), parseInt(this.anketa.q22), parseInt(this.anketa.q23), parseInt(this.anketa.q24), parseInt(this.anketa.q25), parseInt(this.anketa.q26), parseInt(this.anketa.q27), parseInt(this.anketa.q28), parseInt(this.anketa.q29), parseInt(this.anketa.q30), parseInt(this.anketa.q31), parseInt(this.anketa.q32), parseInt(this.anketa.q33), parseInt(this.anketa.q34), parseInt(this.anketa.q35), parseInt(this.anketa.q36), parseInt(this.anketa.q37), parseInt(this.anketa.q38), parseInt(this.anketa.q39), parseInt(this.anketa.q40))
      this.axios
        .post('//127.0.0.1:8000/check_anketa', {
          data: this.check_anketa
        }, {
          headers: {
            'Content-Type': 'application/json'
          }
        })
        .then((response) => {
          console.log(response)
          console.log(response.data)
          if (response.data.prediction[0] === 1) {
            this.axios
              .post('//127.0.0.1:8000/anketa', this.anketa)
              .then((response) => {
                console.log(response)
                if (response.status === 201) {
                  window.location = '/anketa'
                }
              })
          } else {
            this.axios
              .post('//127.0.0.1:8000/anketa_fake', this.anketa)
              .then((response) => {
                console.log(response)
                if (response.status === 201) {
                  window.location = '/anketa'
                }
              })
          }
        })
    },
    updateContext () {
      console.log(this.anketa.hospital)
      console.log(this.anketa.department)
      console.log(this.departments)
      console.log(this.doctors)
      this.departments_names = []
      this.doctors_names = []
      if (this.anketa.hospital !== '') {
        this.departments.forEach((dep) => {
          if (dep.hospital_department === this.anketa.hospital) {
            this.departments_names.push(dep)
          }
        })
      }
      if (this.anketa.department !== '') {
        this.doctors.forEach((doc) => {
          if (doc.department_doctor === this.anketa.department && doc.hospital_doctor === this.anketa.hospital) {
            this.doctors_names.push(doc)
          }
        })
      }
    }
  },
  mounted () {
    this.getContext()
  }
}
</script>
