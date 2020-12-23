<template>
  <!-- <v-container class="grey lighten-5" fluid>
    <v-row>
      <v-col> 
        <div>
          <v-data-table
            :headers="headers"
            :items="categorias"
            item-key="name"
            class="elevation-1 custom-table"
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
  </v-container> -->
  <v-row justify="center">
    <v-dialog v-model="dialog" persistent max-width="290">
      <template v-slot:activator="{ on, attrs }">
        <v-btn color="primary" dark v-bind="attrs" v-on="on">
          Open Dialog
        </v-btn>
      </template>
      <v-card>
        <v-card-title class="headline">
          Use Google's location service?
        </v-card-title>
        <v-card-text
          >Let Google help apps determine location. This means sending anonymous
          location data to Google, even when no apps are running.</v-card-text
        >
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="green darken-1" text @click="dialog = false">
            Disagree
          </v-btn>
          <v-btn color="green darken-1" text @click="dialog = false">
            Agree
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>
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
      dialog: false,
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
