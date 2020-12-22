<template>
  <v-container class="grey lighten-5" fluid>
    <v-row>
      <v-col> 
        <v-card>
          <v-data-table
            :headers="headers"
            :items="clientes"
            item-key="name"
            class="elevation-3"
            :search="search"
            hide-default-footer
          >
            <template v-slot:top>
              <v-text-field
                v-model="search"
                label="Pesquisa"
              ></v-text-field>
            </template>
          </v-data-table>
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import api from "@/utils";

export default {
  name: "Clientes",
  data() {
    return {
      clientes: [],
      clientes_url: "/clientes/",
      headers: [
        { text: "Nome", align: "start", value: "nome" },
        { text: "Email", align: "start", value: "email" },
        { text: "Cadastrado em", align: "start", value: "dt_cadastro" },
      ],
      search: "",
    };
  },
  mounted() {
    this.getClientes();
  },
  methods: {
    getClientes() {
      api
        .get(this.clientes_url)
        .then((response) => {
          this.clientes = response.data;
        })
        .catch((err) => {
          console.error(err);
        });
    },
  },
};
</script>
