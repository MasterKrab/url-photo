<script lang="ts">
  export let checked = false;
  export let slug: string;
  export let label: string;
</script>

<div class="container">
  <label class="container__label" for={slug}>{label}</label>
  <input
    class="container__input"
    type="checkbox"
    bind:checked
    name={slug}
    id={slug}
  />
</div>

<style lang="scss">
  .container {
    display: flex;
    align-items: center;
    gap: 1rem;

    &__input {
      display: grid;
      place-items: center;
      appearance: none;
      background-color: var(--secondary-color);
      width: 1.25em;
      height: 1.25em;
      border-radius: 50%;
      cursor: pointer;

      @media (hover: hover) {
        transition: transform 0.25s ease-in-out;

        &:hover {
          transform: scale(1.1);
        }
      }

      &::before {
        content: "";
        width: 0.75em;
        height: 0.75em;
        background-color: var(--primary-color);
        border-radius: 50%;
        opacity: 0;
        transition: opacity 0.25s ease-in-out;
      }

      &:checked::before {
        opacity: 1;
      }
    }
  }
</style>
