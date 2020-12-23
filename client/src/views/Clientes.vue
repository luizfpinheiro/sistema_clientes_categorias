<template>
  <v-container class="grey lighten-5" fluid>
    <v-row>
      <v-col>
        <v-card>
          <v-card-text>
            <v-dialog v-model="dialog" persistent max-width="600">
              <template v-slot:activator="{ on, attrs }">
                <v-btn
                  color="success"
                  dark
                  absolute
                  top
                  right
                  fab
                  v-bind="attrs"
                  v-on="on"
                >
                  <v-icon>mdi-plus</v-icon>
                </v-btn>
              </template>
              <v-card>
                <v-card-title>
                  <span class="headline">Cliente</span>
                </v-card-title>
                <v-card-text>
                  <v-container>
                    <v-row>
                      <v-col cols="12">
                        <v-text-field
                          v-model="form.nome"
                          label="Nome*"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-text-field
                          v-model="form.email"
                          label="Email*"
                          required
                        ></v-text-field>
                      </v-col>
                      <v-col cols="12">
                        <v-autocomplete
                          v-model="form.tags"
                          :items="tags"
                          label="Categorias"
                          multiple
                        ></v-autocomplete>
                      </v-col>
                    </v-row>
                    <small>*Campos obrigatórios</small>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="black" text @click="fecharEdicaoCliente">
                    Fechar
                  </v-btn>
                  <v-btn color="green darken-1" text @click="cadastrarCliente">
                    Salvar
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-text>

          <v-card-text>
            <v-data-table
              :headers="headers"
              :items="clientes"
              item-key="name"
              class="elevation-3"
              :search="search"
              hide-default-footer
            >
              <template v-slot:top>
                <v-text-field v-model="search" label="Pesquisa"></v-text-field>
              </template>

              <template v-slot:item.tags="{ item }">
                <v-chip v-for="tag in item.tags" :key="tag.id" dark class="ma-1" small>
                  {{ tag.nome }}
                </v-chip>
              </template>

              <template v-slot:item.action="{ item }">
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-icon
                      v-on="on"
                      small
                      class="ma-1"
                      @click="abrirEdicaoCliente(item)"
                      >mdi-pencil</v-icon
                    >
                  </template>
                  <span>Editar</span>
                </v-tooltip>

                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-icon
                      v-on="on"
                      small
                      @click="dialog_excluir = true"
                      class="ma-1"
                      >mdi-delete
                    </v-icon>
                  </template>
                  <span>Excluir</span>
                </v-tooltip>
                <v-dialog v-model="dialog_excluir" persistent max-width="280">
                  <v-card>
                    <v-card-title class="headline">
                      Confirmar exclusão?
                    </v-card-title>
                    <v-card-text>Cliente: {{ item.nome }}</v-card-text>
                    <v-card-actions>
                      <v-spacer></v-spacer>
                      <v-btn
                        color="black darken-1"
                        text
                        @click="dialog_excluir = false"
                      >
                        Cancelar
                      </v-btn>
                      <v-btn
                        color="green darken-1"
                        text
                        @click="excluirCliente(item.id)"
                      >
                        Excluir
                      </v-btn>
                      <v-spacer></v-spacer>
                    </v-card-actions>
                  </v-card>
                </v-dialog>
              </template>
            </v-data-table>
          </v-card-text>
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
      tags: [],
      categorias_url: "/categorias/",
      clientes_url: "/clientes/",
      headers: [
        { text: "Nome", align: "start", value: "nome"},
        { text: "Email", align: "start", value: "email" },
        { text: "Tags", align: "start", value: "tags" },
        { text: "Cadastrado em", align: "start", value: "dt_cadastro" },
        { text: "Ação", value: "action", align: "center", sortable: false },
      ],
      search: "",
      dialog: false,
      modo_edicao: false,
      dialog_excluir: false,
      form: {
        nome: "",
        email: "",
        tags: [],
      },
    };
  },
  mounted() {
    this.getClientes();
    this.getCategorias();
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
    getCategorias() {
      api
        .get(this.categorias_url)
        .then((response) => {
          response.data.forEach((element) => {
            this.tags.push({
              text: element.nome,
              value: element.id,
            });
          });
        })
        .catch((err) => {
          console.error(err);
        });
    },
    cadastrarCliente() {
      this.dialog = false;

      if (this.modo_edicao) {
        let id = this.form.id;
        let tags = [];
        
        this.form.tags.forEach(element => {
          if(element.value) {
            tags.push(element.value)
          }
          else {
            tags.push (element);
          }
        });
        
        this.form.tags = tags;

        api
          .put(this.clientes_url + id + "/", this.form)
          .then((response) => {
            if (response.status == 200) {
              window.location.reload();
            }
          })
          .catch((err) => {
            console.error(err);
          });
      } else {
        api
          .post(this.clientes_url, this.form)
          .then((response) => {
            if (response.status == 201) {
              window.location.reload();
            }
          })
          .catch((err) => {
            console.error(err);
          });
      }
    },
    excluirCliente(id) {
      this.dialog_excluir = false;
      api
        .delete(this.clientes_url + id)
        .then(() => {
          window.location.reload();
        })
        .catch((err) => {
          console.error(err);
        });
    },
    abrirEdicaoCliente(cliente) {
      this.modo_edicao = true;

      this.dialog = true;
      this.form = {
        id: cliente.id,
        nome: cliente.nome,
        email: cliente.email,
        tags: [],
      };

      cliente.tags.forEach((element) => {
        this.form.tags.push({
          text: element.nome,
          value: element.id,
        });
      });
    },
    fecharEdicaoCliente() {
      this.dialog = false;
      this.form = {};
    },
  },
};
</script>
