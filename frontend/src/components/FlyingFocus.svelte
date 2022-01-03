<script lang="ts">
  import FloatingFocus from "@q42/floating-focus-a11y/dist/unstyled";
  import "@q42/floating-focus-a11y/dist/unstyled/index.css";

  let element: HTMLElement;

  $: new FloatingFocus(element);
</script>

<div bind:this={element} />

<style global>
  *:focus {
    outline: none;
  }

  .floating-focus-enabled :focus,
  .floating-focus-enabled .focus {
    outline: #1e90ff solid 2px;
    outline-offset: 8px;
  }

  .floating-focus-enabled [type="button"]:focus {
    outline-color: #008000;
    outline-offset: 4px;
  }
</style>
