<template>
  <v-container class="grey lighten-5" fluid>
    <v-row>
      <v-col> 
        <div>
          <v-data-table
            :headers="headers"
            :items="categorias"
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
import api from "@/utils";

export default {
  name: "Categorias",
  data() {
    return {
      categorias: [],
      categorias_url: "/categorias/",
      headers: [
        { text: "Número", align: "start", value: "id" },
        { text: "Nome", align: "start", value: "nome" },
        { text: "Cadastrada em", align: "start", value: "dt_cadastro" },
      ],
      search: "",
    };
  },
  mounted() {
    this.getCategorias();
  },
  methods: {

    getCategorias() {
      api
        .get(this.categorias_url)
        .then((response) => {
          this.categorias = response.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
