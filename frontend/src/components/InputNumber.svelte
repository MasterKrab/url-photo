<script lang="ts">
  export let value = 0;
  export let min: number;
  export let max: number;
  export let slug: string;
  export let label: string;
</script>

<div class="container">
  <label class="container__label" for={slug}>{label}</label>
  <input
    class="container__input"
    type="number"
    name={slug}
    bind:value
    id={slug}
    {max}
    {min}
  />
</div>

<style lang="scss">
  .container {
    display: grid;
    grid-template-columns: 1fr 3fr;
    align-items: center;
    gap: 0.5rem;
    background-color: var(--secondary-color);
    padding: 0.5rem 0.75rem 0.5rem 0.5rem;
    border: 2px solid transparent;
    border-radius: 0.25rem;
    font-weight: bold;
    color: var(--primary-color);
    overflow: hidden;

    &__input {
      border: none;
      background-color: inherit;
    }
  }
</style>
