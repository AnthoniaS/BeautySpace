<template>
<form class="form-signin mt-5" @submit.prevent="logar">
  <div class="text-center mb-4">
    <h1 class="h3 mb-3 font-weight-normal">Identificação do Usuário</h1>
  </div>

  <div class="form-label-group">
    <input type="email" id="inputEmail" class="form-control" placeholder="Email address" required autofocus
           v-model="email">
    <label for="inputEmail">E-mail do Usuário</label>
  </div>

  <div class="form-label-group">
    <input type="password" id="inputPassword" class="form-control" placeholder="Password" required
           v-model="senha">
    <label for="inputPassword">Senha de Acesso</label>
  </div>

  <button class="btn btn-lg btn-success btn-block" type="submit">Entrar</button>
</form>    
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            email: null,
            senha: null
        }
    },
    methods: {
        logar() {
            axios.post(this.$urlAPI+'/login_cliente', {email: this.email, senha: this.senha})
                 .then(response => {
                     if (response.data.user == null) {
                         alert('Erro... Login ou senha inválidos')
                     } else {
                         localStorage.setItem('token', response.data.access_token)
                         this.$parent.mudaUser(response.data.user)
                         this.$router.push('/')
                     }
                 })
        }
    }
}
</script>

<style scoped>
template {
  height: 100%;
  display: -ms-flexbox;
  display: flex;
  -ms-flex-align: center;
  align-items: center;
  padding-top: 40px;
  padding-bottom: 40px;
  background-color: #f5f5f5;
}

.form-signin {
  width: 100%;
  max-width: 420px;
  padding: 15px;
  margin: auto;
}

.form-label-group {
  position: relative;
  margin-bottom: 1rem;
}

.form-label-group > input,
.form-label-group > label {
  height: 3.125rem;
  padding: .75rem;
}

.form-label-group > label {
  position: absolute;
  top: 0;
  left: 0;
  display: block;
  width: 100%;
  margin-bottom: 0; /* Override default `<label>` margin */
  line-height: 1.5;
  color: #495057;
  pointer-events: none;
  cursor: text; /* Match the input under the label */
  border: 1px solid transparent;
  border-radius: .25rem;
  transition: all .1s ease-in-out;
}

.form-label-group input::-webkit-input-placeholder {
  color: transparent;
}

.form-label-group input:-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-ms-input-placeholder {
  color: transparent;
}

.form-label-group input::-moz-placeholder {
  color: transparent;
}

.form-label-group input::placeholder {
  color: transparent;
}

.form-label-group input:not(:placeholder-shown) {
  padding-top: 1.25rem;
  padding-bottom: .25rem;
}

.form-label-group input:not(:placeholder-shown) ~ label {
  padding-top: .25rem;
  padding-bottom: .25rem;
  font-size: 12px;
  color: #777;
}

/* Fallback for Edge
-------------------------------------------------- */
@supports (-ms-ime-align: auto) {
  .form-label-group > label {
    display: none;
  }
  .form-label-group input::-ms-input-placeholder {
    color: #777;
  }
}

/* Fallback for IE
-------------------------------------------------- */
@media all and (-ms-high-contrast: none), (-ms-high-contrast: active) {
  .form-label-group > label {
    display: none;
  }
  .form-label-group input:-ms-input-placeholder {
    color: #777;
  }
}
</style>