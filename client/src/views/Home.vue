<template>
  <v-container class="grey lighten-5" fluid>
    <v-row>
      <v-col>
        <v-card>
          <v-navigation-drawer class="deep-purple accent-4" width="100%">
            <v-list>
              <v-list-item v-for="item in items" :key="item.title" link>
                <v-list-item-icon>
                  <v-icon>{{ item.icon }}</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                  <v-list-item-title>{{ item.title }}</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-navigation-drawer>
        </v-card>
      </v-col>
      <v-divider class="mx-4" vertical></v-divider>
      <v-col cols="9">
        <div>
          <v-data-table
            :headers="headers"
            :items="desserts"
            item-key="name"
            class="elevation-1"
            :search="search"
            hide-default-footer
          >
            <template v-slot:top>
              <v-text-field
                v-model="search"
                label="Pesquisa"
                class="mx-4"
              ></v-text-field>
            </template>
          </v-data-table>
        </div>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
// import HelloWorld from '@/components/HelloWorld.vue'
import { get, post, update, remove } from '@/utils'

export default {
  name: "Home",
  data() {
    return {
      clientes: [],
      categorias: [],
      clientes_url: 'localhost:8000/clientes',
      categorias_url: 'localhost:8000/categorias',
      items: [
        { title: "Clientes", icon: "mdi-account-box" },
        { title: "Categorias", icon: "mdi-view-dashboard" },
      ],
      search: "",
      calories: "",
      headers: [
        {
          text: "Dessert (100g serving)",
          align: "start",
          sortable: false,
          value: "name",
        },
        {
          text: "Calories",
          value: "calories",
        },
        { text: "Fat (g)", value: "fat" },
        { text: "Carbs (g)", value: "carbs" },
        { text: "Protein (g)", value: "protein" },
        { text: "Iron (%)", value: "iron" },
      ],
      desserts: [
        {
          name: "Frozen Yogurt",
          calories: 159,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%",
        },
        {
          name: "Ice cream sandwich",
          calories: 237,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%",
        },
      ],
    };
  },
  methods: {
    getClientes() {
      this.clientes = get(this.clientes_url);
    },
    getCategorias() {
      this.categorias = get(this.categorias_url);
    },
    removerItem(url, id) {
      this.clientes = remove(url + '/' + id);
    },
    atualizarItem(url, id, params) {
      update(url + '/' + id, params);
    },
    criarItem(url, params) {
      post(url, params)
    }
  }
};
</script>
