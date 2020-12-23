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
                  <span class="headline">Tag</span>
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
                    </v-row>
                    <small>*Campos obrigatórios</small>
                  </v-container>
                </v-card-text>
                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="black" text @click="fecharEdicaoCategoria">
                    Fechar
                  </v-btn>
                  <v-btn
                    color="green darken-1"
                    text
                    @click="cadastrarCategoria"
                  >
                    Salvar
                  </v-btn>
                </v-card-actions>
              </v-card>
            </v-dialog>
          </v-card-text>

          <v-card-text>
            <v-data-table
              :headers="headers"
              :items="categorias"
              item-key="name"
              class="elevation-3"
              :search="search"
              hide-default-footer
            >
              <template v-slot:top>
                <v-text-field v-model="search" label="Pesquisa"></v-text-field>
              </template>

              <template v-slot:item.qtd_clientes="{ item }">
                <v-chip
                  dark
                  class="ma-1 success"
                  small
                >
                  {{ item.qtd_clientes }}
                </v-chip>
              </template>

              <template v-slot:item.action="{ item }">
                <v-tooltip top>
                  <template v-slot:activator="{ on }">
                    <v-icon
                      v-on="on"
                      small
                      class="ma-1"
                      @click="abrirEdicaoCategoria(item)"
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
                    <v-card-text>Tag: {{ item.nome }}</v-card-text>
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
                        @click="excluirCategoria(item.id)"
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
  name: "Categorias",
  data() {
    return {
      categorias: [],
      categorias_url: "/categorias/",
      headers: [
        { text: "Nome da Tag", align: "start", value: "nome" },
        {
          text: "Quantidade de Clientes",
          align: "start",
          value: "qtd_clientes",
        },
        { text: "Cadastrado em", align: "start", value: "dt_cadastro" },
        { text: "Ação", value: "action", align: "center", sortable: false },
      ],
      search: "",
      dialog: false,
      modo_edicao: false,
      dialog_excluir: false,
      form: {
        nome: "",
      },
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
    cadastrarCategoria() {
      this.dialog = false;

      if (this.modo_edicao) {
        let id = this.form.id;

        api
          .put(this.categorias_url + id + "/", this.form)
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
          .post(this.categorias_url, this.form)
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
    excluirCategoria(id) {
      this.dialog_excluir = false;
      api
        .delete(this.categorias_url + id)
        .then(() => {
          window.location.reload();
        })
        .catch((err) => {
          console.error(err);
        });
    },
    abrirEdicaoCategoria(categoria) {
      this.modo_edicao = true;

      this.dialog = true;
      this.form = {
        id: categoria.id,
        nome: categoria.nome,
        email: categoria.email,
        tags: [],
      };
    },
    fecharEdicaoCategoria() {
      this.dialog = false;
      this.form = {};
    },
  },
};
</script>
