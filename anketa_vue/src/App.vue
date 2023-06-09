<template>
  <v-app >
    <v-navigation-drawer dark color="#263238" v-model="drawer" app>
      <v-list dense nav>
        <v-list-item v-for="item in items" :key="item.title" :to="item.to" link>
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item @click="logout" v-if="token === true" link>
          <v-list-item-icon>
            <v-icon> {{ 'mdi-logout' }} </v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title>Выход</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-sheet
      class="overflow-y-auto"
      max-height="1009">
      <v-container>
        <v-main>
          <router-view>
          </router-view>
        </v-main>
      </v-container>
    </v-sheet>
  </v-app>
</template>

<script>
export default {
  data: () => ({
    drawer: null,
    token: false,
    items: []
  }),
  methods:
  {
    checkLogin () {
      var ref
      if (sessionStorage.getItem('auth_token') !== null) {
        this.token = true
        ref = '/menu'
      } else {
        ref = '/account'
      }
      this.items = [
        { title: 'Анкета', icon: 'mdi-notebook-edit-outline', to: '/anketa' },
        { title: 'Статистика', icon: 'mdi-google-analytics', to: ref }
      ]
    },
    logout () {
      sessionStorage.removeItem('auth_token')
      window.location = '/anketa'
    }
  },
  mounted () {
    this.checkLogin()
  }
}

</script>
<style>
.mb-footer {
  margin-bottom: 190px;
}
</style>
